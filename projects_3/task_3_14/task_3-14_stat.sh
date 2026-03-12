#!/bin/bash

echo "--- Статистика по оценкам ---"

awk '
   NR > 0
    { 
        sum += $2           
    } 
    END { 
        print "Сумма всех оценок: " sum
        print "Средняя оценка: " sum / NR
    }
'  students.txt

awk 'NR==1{max=$2} $2>max{max=$2} END{print "Максимальная оценка: " max}' students.txt 
