solution_volume = float(input("Введите нужный объем раствора (мл): "))
salt_mass = solution_volume * 0.009
water_volume = solution_volume

with open("/Users/macbook/Desktop/Горохова_АИ/recipe1.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    recipe.write("-" * 23)
    recipe.write(f"\nОбщий объем:\t{solution_volume} мл\nМасса соли:\t{salt_mass:.2f} г\nОбъем воды:\t{water_volume} мл")

print("Данные успешно сохранены в файл.")