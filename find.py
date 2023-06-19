def find_person(surname: str):
    with open('test.txt', 'r', encoding='utf-8') as file:
        line_list = file.read().splitlines()
        found = False
        for ind in range(len(line_list)):
            if line_list[ind] == surname.title():
                found = True
                print(line_list[ind])
                print(line_list[ind + 1])
                print(line_list[ind + 2])
                print(line_list[ind + 3])
                print()
        if not found:
            print('Контакт не найден!')
