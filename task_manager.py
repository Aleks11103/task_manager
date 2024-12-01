import json

from task import Task


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

    # Вывод списка задач на экран
    def __str__(self):
        return "\n".join([el.__str__() for el in self.tasks_list])

    # Создание новой задачи
    def new_task(
        self, title, description, category, due_date, priority, status
    ):
        self.tasks_list.append(
            Task(title, description, category, due_date, priority, status)
        )

    # Редактирование задачи по ID
    def edit_task(
        self, id, title, description, category, due_date, priority, status
    ):
        for task in self.tasks_list:
            if task.id != id:
                continue
            task.title = title
            task.description = description
            task.category = category
            task.due_date = due_date
            task.priority = priority
            task.status = status
            break

    # Редактирование статуса задачи
    def edit_status_task(self, id):
        for task in self.tasks_list:
            if task.id != id:
                continue
            task.status = "выполнена"
            break

    # Удаление задачи по идентификатору
    def del_task_id(self, id):
        for task in self.tasks_list:
            if task.id != id:
                continue
            del task
            break

    # Удаление задачи по категории
    def del_task_category(self, category):
        for task in self.tasks_list:
            if task.category != category:
                continue
            del task
            break
