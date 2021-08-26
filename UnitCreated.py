import random


class UnitCreated:

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    id = property(get_id, set_id)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_id, set_id)

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    health = property(get_health, set_health)

    def get_exp(self):
        return self.__experience

    def set_exp(self, exp):
        self.__experience = exp

    experience = property(get_exp, set_exp)

    def get_rank(self):
        return self.__rank

    def set_rank(self, rank):
        self.__rank = rank

    rank = property(get_rank, set_rank)

    def get_atk(self):
        return self.__attack

    def set_atk(self, atk):
        self.__attack = atk

    attack = property(get_atk, set_atk)

    def get_def(self):
        return self.__defence

    def set_def(self, defence):
        self.__defence = defence

    defence = property(get_def, set_def)

    def get_type(self):
        return self.type

    type = property(get_type)  # 0 = tanker 1 = warrior

    def get_pro(self):
        return self.__profession

    profession = property(get_pro)

    def __init__(self, name, type, id):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__health = 100
        self.__experience = 0
        self.__rank = 1
        if self.__type == 0:
            self.__attack = random.randint(1, 10)
            self.__defence = random.randint(5, 15)
            self.__profession = "Tanker"
        else:
            self.__attack = random.randint(5, 20)
            self.__defence = random.randint(1, 10)
            self.__profession = "Warrior"

    def print_attr(self):
        if self.__health > 0:
            print("[ID:{}, NAME:{}, profession:{}, HP:{}, EXP:{}, RANK:{}, ATK:{}, DEF:{}]"
                  .format(self.__id, self.__name, self.__profession, self.__health,
                          self.__experience, self.__rank, self.__attack, self.__defence))
        else:
            print("[Dead][ID:{}, NAME:{}, profession:{}, HP:{}, EXP:{}, RANK:{}, ATK:{}, DEF:{}]"
                  .format(self.__id, self.__name, self.__profession, self.__health,
                          self.__experience, self.__rank, self.__attack, self.__defence))

    def state_check(self):
        if self.__health > 0:
            return 1
        else:
            return 0

    def upgrade(self):
        if self.__experience >= 100:
            print("'{}' is upgrated !".format(self.__name))
            self.__experience = self.__experience - 100
            self.__rank = self.__rank + 1
            if self.__type == 1:
                self.__health = self.__health + random.randint(10, 30)
                self.__attack = self.__attack + random.randint(3, 6)
                self.__defence = self.__defence + random.randint(1, 3)

            else:
                self.__health = self.__health + random.randint(30, 50)
                self.__attack = self.__attack + random.randint(1, 3)
                self.__defence = self.__defence + random.randint(3, 6)
