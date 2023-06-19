def find_person(surname: str):
    with open('test.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if line[:-1] == surname:
                print(line.strip())
                print(file.readline().strip())
                print(file.readline().strip())
                print(file.readline().strip())
                print()