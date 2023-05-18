#!/bin/bash
echo "Введите логин:"
read $REPLY
echo "Введите пароль:"
read $REPLY
let number=$RANDOM
if [ $number -gt 25000 ]
then
echo "У вас на балансе 10000$ хотите снять?"
elif [ $number -gt 50000 ]
then
echo "Может уйдем пораньше сегодня?"
else
echo "Какой ваш любимый язык программирования?"
fi
read $REPLY