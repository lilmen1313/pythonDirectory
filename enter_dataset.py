def input_dataset():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    return surname, name, patronymic, phone


def inp_surname():
    surname = input('Введите фамилию для поиска контакта: ')
    return surname