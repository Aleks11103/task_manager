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
        ) + "\n"
