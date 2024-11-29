import json


class Task:
    __id__ = 1  # id задачи, увелчивающийся с созданием новой задачи

    def __init__(
        self, title, description, category, due_date, priority, status
    ):
        self.id = self.__id__
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status
        Task.__id__ += 1

    def __str__(self):
        return "\n".join(
            (
                str(self.id),
                self.title,
                self.description,
                self.category,
                self.due_date,
                self.priority,
                self.status,
            )
        )


class TaskManager:
    def __init__(self):
        with open("tasks.json", encoding="UTF-8") as f:
            lst = json.load(f)
        self.tasks_list = []
        max_id = 1
        for el in lst:
            task = Task(
                el["title"],
                el["description"],
                el["category"],
                el["due_date"],
                el["priority"],
                el["status"],
            )
            self.tasks_list.append(task)
            if el["id"] > max_id:
                max_id = el["id"]
        Task.__id__ = max_id + 1

    def __str__(self):
        return "\n".join([el.__str__() for el in self.tasks_list])

    def new_task(self):
        pass


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
