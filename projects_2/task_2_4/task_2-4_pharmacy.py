number_of_capsules = int(input("Введите общее количество произведенных капсул: "))
packing_capacity = int(input("Введите количество капсул в одной упаковке: "))

complete_packages = number_of_capsules // packing_capacity
remaining_capsules = number_of_capsules % packing_capacity

print(f"--- Отчет фасовочного цеха ---\nПолных упаковок:\t{complete_packages}\nОстаток капсул:\t{remaining_capsules}")