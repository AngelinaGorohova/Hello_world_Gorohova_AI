name_of_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации (°C): ")
name_for_file = name_of_medium.upper()

with open("/Users/macbook/Desktop/Горохова_АИ/recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"{name_for_file}\n")
    recipe.write(f"Концентрация агара (%): {agar_concentration}\nТемпература стерилизации (°C): {sterilization_temperature}")

print("Файл 'recipe.txt' успешно сформирован!")