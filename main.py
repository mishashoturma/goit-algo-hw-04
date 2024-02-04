
def total_salary(path):
    try:
        with open(path, "r") as file1:
            lines = [el.strip() for el in file1.readlines()]
            total = 0
            person = 0 
            for line in lines:
                part = line.split(',')
                total = total + int(part[1])
                person = person + 1
            average = total / person
            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print("Файл не знайдено")

total_salary("C:/Hw4/salary_file.txt.txt")


    