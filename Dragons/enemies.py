# coding: utf-8
# license: GPLv3

from gameunit import *
from random import randint, choice


def check_prime_number(x):
    check = 0
    for i in range(1, x):
        if x % i == 0:
            check += 1
    if check < 2:
        return ('да')
    else:
        return ('нет')


def check_multiplier(x):
    check = 0
    check_list = []
    for i in range(1, x):
        if x % i == 0:
            check += 1
            check_list.append(i)
    check_list.append(x)
    return (check_list)


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_dragon_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


def generate_troll_list(enemy_number):
    enemy_list = [generate_random_troll() for i in range(enemy_number)]
    return enemy_list


def generate_random_troll():
    RandomEnemyType = choice(enemy_troll_types)
    enemy = RandomEnemyType()
    return enemy


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зеленый'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 300
        self._attack = 15
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 1000
        self._attack = 5
        self._color = 'черный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class CleverTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 15
        self._color = 'умный тролль'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest


class TrollBrute(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 15
        self._color = 'сильный тролль'

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Простое ли число ' + str(x) + '?'
        self.set_answer(check_prime_number(x))
        return self.__quest


class SuperCleverTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 15
        self._color = 'тролль из физтеха'

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Разложи число ' + str(x) + ' на множители и перечисли их по порядку'
        self.set_answer(check_multiplier(x))
        return self.__quest


enemy_dragon_types = [GreenDragon, RedDragon, BlackDragon]
enemy_troll_types = [CleverTroll, SuperCleverTroll, TrollBrute]
