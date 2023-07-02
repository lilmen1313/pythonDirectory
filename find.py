def find_person(surname: str):
    with open('C:/Users/lilme/Desktop/TESTING(Seminar)/Python (Task - directory)/pythonDirectory/test.txt', 'r', encoding='utf-8') as file:
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