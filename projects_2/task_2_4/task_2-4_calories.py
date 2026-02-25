protein = int(input("Введите массу белков в продукте (г): "))
fat = int(input("Введите массу жиров в продукте (г): "))
carbohydrate = int(input("Введите массу углеводов в продукте (г): "))

cal = (protein * 4) + (fat * 9) + (carbohydrate * 4)

print(f"Общая калорийность: {cal}")