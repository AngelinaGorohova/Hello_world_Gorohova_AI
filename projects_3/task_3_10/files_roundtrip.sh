#!/bin/bash

echo "Создаем файлы..."
for i in {1..10}
do
    touch "test$i.txt"
    echo "Создан файл: test$i.txt"
done

echo "-----------------------"
echo "Удаляем файлы..."
COUNT=10

while [ $COUNT -ge 1 ]
do
    rm "test$COUNT.txt"
    echo "Удален файл: test$COUNT.txt"
    
    let "COUNT--"
done

echo "Готово!"