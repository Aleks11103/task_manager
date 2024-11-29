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

    def __str__(self):
        return "\n".join([el.__str__() for el in self.tasks_list])

    def new_task(self):
        pass
