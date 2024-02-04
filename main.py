def get_cats_info(path):
    try:
        with open(path, "r") as file:
            cats_info = []
            lines = [el.strip() for el in file.readlines()]
            for line in lines:
                part = line.split(',')
                cats_info.append({"id": part[0], "name": part[1], "age": part[2], /n})
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено")

print(get_cats_info("C:/Hw4/cats.txt"))



    