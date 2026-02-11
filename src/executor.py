from dataclasses import dataclass
from time import sleep
from typing import Iterable, Type

from plugin.plugin import Plugin

@dataclass
class Task:
  name: str
  sleep_secs: int
  should_fail: bool

  def execute(self):
    if self.should_fail:
      raise RuntimeError("error!!!")
    sleep(self.sleep_secs)
  

class DummyExecutor:
  def __init__(self,
               pipeline_uuid: str,
               tasks: Iterable[Task],
               plugins_classes: Iterable[Type[Plugin]]) -> None:
    self._pipeline_uuid = pipeline_uuid
    self._tasks = tasks
    self._plugins = [p(pipeline_uuid) for p in plugins_classes]

  def execute(self):
    try:
      print(f"pipeline '{self._pipeline_uuid}' started")
      [p.on_pipeline_start() for p in self._plugins]

      for task in self._tasks:
          self._bind_plugins_to_task_execution(task)()

      [p.on_pipeline_success() for p in self._plugins]
      print(f"pipeline finished successfully")
    except Exception as e:
      [p.on_pipeline_failure(e) for p in self._plugins]
      print(f"pipeline failed")
      raise
  
  def _bind_plugins_to_task_execution(self, task:Task):
    def _inner(*args, **kwargs):
      try:
        print(f"task '{task.name} execution started'")
        [p.on_task_start(task.name) for p in self._plugins]

        task.execute(*args, **kwargs)

        [p.on_task_success(task.name) for p in self._plugins]
        print(f"task '{task.name} execution finished - SUCCESS'")
      except:
        print(f"task '{task.name} execution finished - FAILED'")
        [p.on_task_failure(task.name) for p in self._plugins]
        raise
    return _inner
  