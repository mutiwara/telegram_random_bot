import random


def dice_photo(number):
    if number == 1:
        photo = open('photo/1.jpg', 'rb')
    if number == 2:
        photo = open('photo/2.jpg', 'rb')
    if number == 3:
        photo = open('photo/3.jpg', 'rb')
    if number == 4:
        photo = open('photo/4.jpg', 'rb')
    if number == 5:
        photo = open('photo/5.jpg', 'rb')
    if number == 6:
        photo = open('photo/6.jpg', 'rb')
    return photo


def password_creater(length):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '1234567890'
    string = lower + upper + number
    try:
        password = ''.join(random.sample(string, length))
        return password
    except Exception:
        return False
