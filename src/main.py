import random
import uuid
from executor import DummyExecutor, Task
from plugin.logger_plugin import LoggerPlugin

NUM_OF_TASKS = 5
PLUGINS = [LoggerPlugin]
SHOULD_FAIL = False

uuid = str(uuid.uuid4())
tasks = [Task(name=f"task-{i}",
              sleep_secs=random.randint(0,3),
              should_fail=SHOULD_FAIL and i > NUM_OF_TASKS/2) for i in range(NUM_OF_TASKS)]

DummyExecutor(pipeline_uuid=uuid,
              tasks=tasks,
              plugins_classes=PLUGINS).execute()