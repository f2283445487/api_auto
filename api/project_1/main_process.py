from api.project_1.test_task.test_task import test_task
from api.project_1.engine.engine import Interface


class MainProcess(object):
    test_task = test_task
    interface = Interface()
    interface.execute_process(test_task)
    interface.result()
