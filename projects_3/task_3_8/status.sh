#!/bin/bash

USER=$(whoami)
TIME=$(date +"%H:%M:%S")
PWD=$(pwd)

echo "Пользователь: $USER"
echo "Текущее время: $TIME"
echo "Путь: $PWD"
echo "Количество переданных аргументов: $#"

