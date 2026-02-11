from abc import ABCMeta

class Plugin(metaclass=ABCMeta):
  def __init__(self, pipeline_uuid: str) -> None:
    self._pipeline_uuid = pipeline_uuid

  def on_pipeline_start(self):
    raise NotImplementedError()

  def on_task_start(self, task_name: str):
    raise NotImplementedError()

  def on_task_success(self, task_name: str):
    raise NotImplementedError()

  def on_task_failure(self, task_name: str):
    raise NotImplementedError()

  def on_pipeline_success(self):
    raise NotImplementedError()

  def on_pipeline_failure(self, e: Exception):
    raise NotImplementedError()