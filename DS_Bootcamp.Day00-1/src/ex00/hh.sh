#!/bin/sh

RESULT_FILE="./hh.json"
NUMBER_OF_VACANSIES="20"

if [ $# = 1 ]; then
    curl -G "https://api.hh.ru/vacancies?text=$1&page=0&per_page=$NUMBER_OF_VACANSIES" | jq > $RESULT_FILE
else
    echo "Скрипту нужно передать название вакансии в качестве аргумента"
    echo "Напрмиер: ./hh.sh 'data-scientist'"
fi