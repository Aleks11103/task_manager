from check import check_date, check_id, check_str
from task_manager import TaskManager

task_manager = TaskManager()
while True:
    print(
        "\n".join(
            (
                "\nВыберите номер действия:",
                "0. Выход",
                "1. Показать весь список задач",
                "2. Просмотр задач по категории",
                "3. Добавление новой задачи",
                "4. Редактирование существующей задачи",
                "5. Отметка о выполнении задачи",
                "6. Удаление задачи по номеру",
                "7. Удаление задач по категории",
                "8. Поиск по ключевым словам в названии задачи",
                "9. Поиск по статусу выполнения",
                "10. Сохранить данные в файл",
            )
        )
    )
    while True:
        command = input("Укажите номер комманды для выполнения: ")
        if command.isdigit():
            command = int(command)
            if 0 <= command <= 10:
                break
        else:
            print("Ошибка! Неверный ввод!")
    match command:
        case 0:  # Сохранение данных в файл и завершение работы программы
            task_manager.add_data_to_json()
            break
        case 1:  # Отображение всего списка задач
            print("\nСПИСОК ЗАДАЧ:\n")
            print(task_manager)
        case 2:  # Отображение задач по категории
            message = "\nВведите название категории для отображения: "
            category = check_str(input(message), message)
            print(f"СПИСОК ЗАДАЧ ПО КАТЕГОРИИ: {category.capitalize()}")
            task_manager.show_category_tasks(category)
        case 3:  # Добавление новой задачи
            mess_title = "\nНазвание задачи: "
            title = check_str(input(mess_title), mess_title)
            mess_desc = "Описание задачи: "
            description = check_str(input(mess_desc), mess_desc)
            mess_cat = "Название категории для задачи: "
            category = check_str(input(mess_cat), mess_cat)
            mess_date = "Конечный срок задачи в формате(ГГГГ-ММ-ДД): "
            due_date = check_date(input(mess_date), mess_date)
            mess_prior = "Уровень приоритета для задачи: "
            priority = check_str(input(mess_prior), mess_prior)
            task_manager.new_task(
                title, description, category, due_date, priority
            )
        case 4:  # Редактирование существующей задачи
            print(task_manager)
            mess_id = "\nВведите номер записи для редактирования: "
            id = check_id(input(mess_id), mess_id, task_manager)
            print(f"ЗАДАЧА С НОМЕРОМ {id}:\n")
            task_manager.show_number_task(id)
            print("\nВведите новые значения для редактируемых полей")
            print("*поля без редактирования пропустите вводом пустой строки")
            mess_title = "Название задачи: "
            title = check_str(input(mess_title), mess_title, empty=True)
            mess_desc = "Описание задачи: "
            description = check_str(input(mess_desc), mess_desc, empty=True)
            mess_cat = "Название категории для задачи: "
            category = check_str(input(mess_cat), mess_cat, empty=True)
            mess_date = "Конечный срок задачи в формате(ГГГГ-ММ-ДД): "
            due_date = check_date(input(mess_date), mess_date, empty=True)
            mess_prior = "Уровень приоритета для задачи: "
            priority = check_str(input(mess_prior), mess_prior, empty=True)
            mess_status = "Статус задачи: "
            status = check_str(input(mess_status), mess_status, empty=True)
            task_manager.edit_task(
                id, title, description, category, due_date, priority, status
            )
        case 5:  # Отметка о выполнении задачи
            print(task_manager)
            mess_id = "\nВведите номер выполненной задачи: "
            id = check_id(input(mess_id), mess_id, task_manager)
            task_manager.ready_status_task(id)
        case 6:  # Удаление задачи по номеру
            print(task_manager)
            mess_id = "\nВведите номер удаляемой записи: "
            id = check_id(input(mess_id), mess_id, task_manager)
            task_manager.del_task_id(id)
        case 7:  # Удаление задач по категории
            print(task_manager, task_manager)
            mess_cat = "\nВведите удаляемую категорию: "
            category = check_str(input(mess_cat), mess_cat)
            task_manager.del_task_category(category)
        case 8:  # Поиск по ключевым словам в названии задачи
            mess_word = "\nВведите слово для поиска в названиях задач: "
            key_word = check_str(input(mess_word), mess_word)
            task_manager.search_by_key_word(key_word)
        case 9:  # Поиск по статусу выполнения
            mess_status = "\nВведите статус задач для выборки: "
            status = check_str(input(mess_status), mess_status)
            task_manager.search_by_status(status)
        case 10:  # Сохранить данные в файл
            task_manager.add_data_to_json()
            print("Данные успешно сохранены в файл")
