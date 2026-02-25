print(f"=== Анализ последовательности ДНК ===")

dna = input("Введите последовательность ДНК: ")
DNA = dna.upper()

count_A = DNA.count("A")
count_T = DNA.count("T")
count_G = DNA.count("G")
count_C = DNA.count("C")

len = len(DNA)

percent_А = count_A / len * 100
percent_T = count_T / len * 100
percent_G = count_G / len * 100
percent_C = count_C / len * 100

print(f"Последовательность в верхнем регистре: {DNA}\nПодсчет нуклеотидов:\nA:\t{count_A}\nT:\t{count_T}\nG:\t{count_G}\nC:\t{count_C}")
print(f"Общая длина: {len} нуклеотидов")
print(f"Процентное содержание (%):\nA:\t{percent_А:.2f}\nT:\t{percent_T:.2f}\nG:\t{percent_G:.2f}\nC:\t{percent_C:.2f}")
