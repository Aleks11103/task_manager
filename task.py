class Task:
    __id__ = 1  # id задачи, увелчивающийся с созданием новой задачи

    def __init__(
        self,
        title: str,
        description: str,
        category: str,
        due_date: str,
        priority: str,
        status="не выполнена"
    ) -> None:
        self.id = self.__id__
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status
        Task.__id__ += 1

    def __str__(self) -> str:
        return (
            "\n".join(
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
            + "\n"
        )

    # Редактирование задачи
    def edit_task(
        self,
        title: str,
        description: str,
        category: str,
        due_date: str,
        priority: str,
        status: str
    ) -> None:
        if title:
            self.title = title
        if description:
            self.description = description
        if category:
            self.category = category
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority
        if status:
            self.status = status

    # Установка задаче статуса готовности
    def ready_status_task(self) -> None:
        self.status = "Выполнена"

    # Упаковка данных в словарь
    def dict_task(self) -> None:
        task_dict = {}
        task_dict["id"] = self.id
        task_dict["title"] = self.title
        task_dict["description"] = self.description
        task_dict["category"] = self.category
        task_dict["due_date"] = self.due_date
        task_dict["priority"] = self.priority
        task_dict["status"] = self.status
        return task_dict
