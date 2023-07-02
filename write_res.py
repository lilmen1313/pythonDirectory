def write_person(dataset: tuple):
    """Функция для записи в файл нового контакта"""
    with open('C:/Users/lilme/Desktop/TESTING(Seminar)/Python (Task - directory)/pythonDirectory/test.txt', 'a', encoding='utf-8') as file:
        file.write('\n\n' + '\n'.join(dataset))