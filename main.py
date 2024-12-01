from task_manager import TaskManager

task_manager = TaskManager()
# task1 = Task(
#     "Проверка навыков Python",
#     "Прохождение теста на проверку навыков",
#     "Обучение",
#     "2024-12-01",
#     "Высокий",
#     "Не выполнена",
# )
# print(task1)
while True:
    print("0. Выход\n \
          1. Показать весь список задач\n \
          2. Просмотр задач по категории\n \
          3. Добавление новой задачи\n \
          4. Редактирование существующейзадачи\n \
          5. Отметка о выполнении задачи\n \
          6. Удаление задачи по номеру\n \
          7. Удаление задач по категории\n \
          ")
    command = int(input("Укажите номер комманды для выполнения: "))
    match command:
        case 0:
            break
        case 1:
            print("СПИСОК ЗАДАЧ:\n\n")
            print(task_manager)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
