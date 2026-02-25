name_of_reagent = input("Введите название нового реактива: ")
number_of_reagent = int(input("Введите его количество: "))

f = open("/Users/macbook/Desktop/Горохова_АИ/projects_2/task_2_2/inventory.txt", "w", encoding="utf-8")
print(f"Реактив \"{name_of_reagent}\" поступил на склад в количестве {number_of_reagent} штук.", file=f)
f.close()