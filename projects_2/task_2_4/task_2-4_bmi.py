weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (cм): "))

bmi = weight / ((height / 100) ** 2)

print(f"--- Отчет о состоянии здоровья ---\nРост:\t{height} см\nВес:\t{weight} кг\nИндекс массы тела:\t{bmi:.2f}")