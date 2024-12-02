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
    def new_task(self, title, description, category, due_date, priority):
        self.tasks_list.append(
            Task(title, description, category, due_date, priority)
        )
        print("Новая задача создана успешно")

    # Отображение задач выбранной категории
    def show_category_tasks(self, category):
        flag = False
        counter = 0
        res = []
        for task in self.tasks_list:
            if task.category.capitalize() != category:
                continue
            res.append(task.__str__())
            flag = True
            counter += 1
        if flag:
            print("\n".join(res))
            print(f"Найдено {counter} задач(-а/-и)")
        else:
            print("Нет задач в данной категории!")

    # Отображение задачи по номеру
    def show_number_task(self, id):
        for task in self.tasks_list:
            if task.id != id:
                continue
            print(task)
            break

    # Редактирование задачи по ID
    def edit_task(
        self, id, title, description, category, due_date, priority, status
    ):
        for task in self.tasks_list:
            if task.id != id:
                continue
            task.edit_task(
                title, description, category, due_date, priority, status
            )
            break
        print(f"Задача {id} отредактирована успешно")

    # Отметка готовности статуса задачи
    def ready_status_task(self, id):
        for task in self.tasks_list:
            if task.id != id:
                continue
            task.ready_status_task()
            break
        print(f"Статус задачи {id}: выполнена")

    # Удаление задачи по идентификатору
    def del_task_id(self, id):
        for task in self.tasks_list:
            if task.id != id:
                continue
            self.tasks_list.remove(task)
            break
        print("Задача {id} удалена")

    # Удаление задачи по категории
    def del_task_category(self, category):
        counter = 0
        for task in self.tasks_list:
            if task.category != category:
                continue
            self.tasks_list.remove(task)
            counter += 1
            break
        print(f"Удалено {counter} задач(-а/-и)")

    # Добавление данных в файл
    def add_data_to_json(self):
        data = []
        for task in self.tasks_list:
            data.append(task.dict_task())
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    # Поиск в названии по ключевому слову
    def search_by_key_word(self, key_word):
        print(f"\nСписок задач содержащих в названии: {key_word}")
        for task in self.tasks_list:
            if key_word.lower() in task.title.lower():
                print(task)

    # Поиск по статусу
    def search_by_status(self, status):
        print(f"\nСписок задач по статусу: {status}")
        for task in self.tasks_list:
            if status.lower() == task.status.lower():
                print(task)
