from datetime import datetime as dt


class Player:
    """тестовый класс для усвоения темы"""
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self, numb):
        self.__lvl += Player.__tst(numb)
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod
    def set_new_val(cls, lvl=1, health=100):
        cls.__LVL = Player.__tst(lvl)
        cls.__HEALTH = Player.__tst(health)

    @staticmethod
    def __tst(value):
        if isinstance(value,int):
            return value
        else:
            raise TypeError('Type Errorrrrr')

x = Player()
x.lvl = 5.6

while True:
    ans = input('enter y/n')
    if ans == 'y':
        print(x.lvl)
        lvl = int(input('enter points:'))
        x.lvl = lvl
        print(x.lvl)
        continue
    elif ans == 'p':
        Player.set_new_val(10)
        p = Player()
        print(p.lvl)
        continue
    break
