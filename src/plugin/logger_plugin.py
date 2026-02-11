import time
import queue
import threading
from plugin.plugin import Plugin
from connector.logger import LoggerConnector

class LoggerPlugin(Plugin):
    def __init__(self, pipeline_uuid: str):
        super().__init__(pipeline_uuid)
        self.connector = LoggerConnector()
        self.start_time = None
        self.task_start_times = {}
        
        # Async logging setup
        self.log_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.worker_thread = threading.Thread(target=self._log_worker, daemon=True)
        self.worker_thread.start()

    def _log_worker(self):
        """Background thread to process log messages without blocking the pipeline."""
        while not self.stop_event.is_set() or not self.log_queue.empty():
            try:
                # Wait for a message with a timeout to allow checking stop_event
                item = self.log_queue.get(timeout=1)
                if isinstance(item, tuple):
                    msg, kwargs = item
                    self.connector.send(msg, **kwargs)
                self.log_queue.task_done()
            except queue.Empty:
                continue

    def _enqueue_log(self, message=None, **kwargs):
        self.log_queue.put((message, kwargs))

    def on_pipeline_start(self):
        self.start_time = time.time()
        self._enqueue_log(f"new pipeline started: {self._pipeline_uuid}")

    def on_task_start(self, task_name: str):
        self.task_start_times[task_name] = time.time()

    def on_task_success(self, task_name: str):
        runtime = time.time() - self.task_start_times.get(task_name, time.time())
        self._enqueue_log(f"task: {task_name}, status: SUCCESS, runtime: {runtime:.2f}s")

    def on_task_failure(self, task_name: str):
        runtime = time.time() - self.task_start_times.get(task_name, time.time())
        self._enqueue_log(f"task: {task_name}, status: FAILED, runtime: {runtime:.2f}s")

    def on_pipeline_success(self):
        total_runtime = time.time() - self.start_time if self.start_time else 0
        self._enqueue_log(
            f"pipeline: {self._pipeline_uuid}, total_runtime: {total_runtime:.2f}s, status: SUCCESS"
        )
        self._shutdown_worker()

    def on_pipeline_failure(self, e: Exception):
        total_runtime = time.time() - self.start_time if self.start_time else 0
        self._enqueue_log(
            f"pipeline: {self._pipeline_uuid}, total_runtime: {total_runtime:.2f}s, status: FAILED, error: {e}"
        )
        self._shutdown_worker()

    def _shutdown_worker(self):
        """Ensure all logs are sent before the program exits."""
        self.stop_event.set()
        if self.worker_thread.is_alive():
            self.worker_thread.join()