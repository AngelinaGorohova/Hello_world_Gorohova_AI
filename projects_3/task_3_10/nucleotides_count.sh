#!/bin/bash

#Заголовок таблицы
printf "%-20s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
echo "------------------------------------------------------------"

for file in *.fasta
do
    # (! -s проверяет наличие чего-либо в файле)
    if [ ! -s "$file" ]; then
        continue
    fi
#Извлекаем только последовательность (без заголовков >) и считаем каждый нуклеотид отдельно
seq=$(grep -v "^>" "$file")
#объединяем последовательность в одну строку для подсчёта
seq=$(echo "$seq" | tr -d '\n')

    count_A=$(echo "$seq" | grep -o "A" | wc -l)
    count_T=$(echo "$seq" | grep -o "T" | wc -l)
    count_G=$(echo "$seq" | grep -o "G" | wc -l)
    count_C=$(echo "$seq" | grep -o "C" | wc -l)

    #Вывод результата
    printf "%-20s %-7s %-7s %-7s %-7s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done