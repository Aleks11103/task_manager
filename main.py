from task import Task
from task_manager import TaskManager

task_manager = TaskManager()
task1 = Task(
    "Проверка навыков Python",
    "Прохождение теста на проверку навыков",
    "Обучение",
    "2024-12-01",
    "Высокий",
    "Не выполнена",
)
print(task1)
print(task_manager)
