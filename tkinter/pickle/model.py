# -*- coding: utf-8 -*-

import pickle
import os


# 面向对象
class Card(object):
    def __init__(self, card_id):
        self.card_id = card_id


class Bank(object):
    def __init__(self, bank_name):
        self.bank_name = bank_name


def x():
    a = input('请输入:')
    if a == '0':
        return 0

    if a == 'w':
        card = Card("111111")
        bank = Bank('浙商银行')

        i = {'card': card,
             'userinfo': {'name': 'admin', 'passwd': '123456'},
             'bank': bank
             }
        f = open(os.path.join(os.getcwd(), 'pickle.txt'), 'wb')
        pickle.dump(i, f)
        f.close()
        print("写入成功！")
        return 1

    if a == 'r':
        f = open(os.path.join(os.getcwd(), 'pickle.txt'), 'rb')
        user = pickle.load(f)
        f.close()
        print(user)

        print("++" * 10)
        print(user['card'].card_id)
        print(user.get('card').card_id)
        print("++" * 10)

        print(user.get('bank').bank_name)

        print("++" * 10)
        print(user['userinfo']['name'])
        print(user['userinfo']['passwd'])
        print("++" * 10)

        print('读取成功')
        return 2
    return -1


while True:
    b = x()
    if b:
        print("true- %s" % b)
    else:
        print("false-%s" % b)
        break
