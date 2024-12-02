from task_manager import TaskManager

task_manager = TaskManager()
while True:
    print(
        "\n".join(
            (
                "\nВыберите номер действия:",
                "0. Выход",  # +
                "1. Показать весь список задач",  # +
                "2. Просмотр задач по категории",  # + поиск по категории
                "3. Добавление новой задачи",  # +
                "4. Редактирование существующей задачи",  # +
                "5. Отметка о выполнении задачи",  # +
                "6. Удаление задачи по номеру",  # +
                "7. Удаление задач по категории",  # +
                "8. Поиск по ключевым словам в названии задачи",  # +
                "9. Поиск по статусу выполнения",  # +
                "10. Сохранить данные в файл",  # +
            )
        )
    )
    command = int(input("Укажите номер комманды для выполнения: "))
    match command:
        case 0:  # Сохранение данных в файл и завершение работы программы
            task_manager.add_data_to_json()
            break
        case 1:  # Отображение всего списка задач
            print("\nСПИСОК ЗАДАЧ:\n")
            print(task_manager)
        case 2:  # Отображение задач по категории
            category = input("\nВведите название категории для отображения: ")
            print(f"СПИСОК ЗАДАЧ ПО КАТЕГОРИИ: {category.capitalize()}")
            task_manager.show_category_tasks(category)
        case 3:  # Добавление новой задачи
            title = input("\nВведите название задачи: ")
            description = input("Введите описание задачи: ")
            category = input("Введите название категории для задачи: ")
            due_date = input(
                "Введите конечный срок задачи в формате(ГГГГ-ММ-ДД): "
            )
            priority = input("Введите уровень приоритета для задачи: ")
            task_manager.new_task(
                title, description, category, due_date, priority
            )
        case 4:  # Редактирование существующей задачи
            print(task_manager)
            id = int(input("\nВведите номер записи для редактирования: "))
            print(f"ЗАДАЧА С НОМЕРОМ {id}:\n")
            task_manager.show_number_task(id)
            print("\nВведите новые значения для редактируемых полей")
            print("*поля без редактирования пропустите вводом пустой строки")
            title = input("Название задачи: ")
            description = input("Описание задачи: ")
            category = input("Название категории для задачи: ")
            due_date = input("Конечный срок задачи в формате(ГГГГ-ММ-ДД): ")
            priority = input("Уровень приоритета для задачи: ")
            status = input("Статус задачи: ")
            task_manager.edit_task(
                id, title, description, category, due_date, priority, status
            )
        case 5:  # Отметка о выполнении задачи
            print(task_manager)
            id = int(
                input(
                    "\nВведите номер записи для установки статуса выполнено: "
                )
            )
            task_manager.ready_status_task(id)
        case 6:  # Удаление задачи по номеру
            print(task_manager)
            id = int(input("\nВведите номер удаляемой записи: "))
            task_manager.del_task_id(id)
        case 7:  # Удаление задач по категории
            print(task_manager)
            category = input("\nВведите удаляемую категорию: ")
            task_manager.del_task_category(category)
        case 8:  # Поиск по ключевым словам в названии задачи
            key_word = input("\nВведите слово для поиска в названиях задач: ")
            task_manager.search_by_key_word(key_word)
        case 9:  # Поиск по статусу выполнения
            status = input("\nВведите статус задач для выборки: ")
            task_manager.search_by_status(status)
        case 10:  # Сохранить данные в файл
            task_manager.add_data_to_json()
