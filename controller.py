from enter_dataset import inp_surname, input_dataset
from find import find_person
from write_res import write_person


def controller():
    mode = int(input('Выберите режим работы со справочником: (1 - найти контакт, 2 - добавить контакт): '))
    if mode == 1:
        surname = inp_surname()
        find_person(surname)
    elif mode == 2:
        dataset = input_dataset()
        write_person(dataset)
    else:
        print('Такого режима не существует')
        controller()