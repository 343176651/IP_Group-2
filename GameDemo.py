import random
import re
units = []
en_units = []


class UnitCreated:
    id = 0
    name = ""
    health = 100
    experience = 0
    rank = 1
    attack = 0
    defence = 0
    type = 0  # 0 = tanker 1 = warrior
    profession = ""

    def __init__(self, name, type, id):
        self.id = id
        self.name = name
        self.type = type
        if self.type == 0:
            self.attack = random.randint(1, 10)
            self.defence = random.randint(5, 15)
            self.profession = "Tanker"
        else:
            self.attack = random.randint(5, 20)
            self.defence = random.randint(1, 10)
            self.profession = "Warrior"

    def print_attr(self):
        print("[ID:{}, NAME:{}, profession:{}, HP:{}, EXP:{}, RANK:{}, ATK:{}, DEF:{}]"
              .format(self.id, self.name, self.profession, self.health, self.experience,
                      self.rank, self.attack, self.defence))


class CheckUid:
    uid = 0

    @classmethod
    def check(cls, uid_chosen):
        pattern = re.compile('^([0-3])$')
        if pattern.search(uid_chosen) is not None:
            cls.uid = int(uid_chosen)
            return cls.uid
        else:
            cls.uid = random.randint(1, 3)
            return cls.uid


def main():
    attr = []
    en_attr = []
    print("===Create your unit===")
    global units
    for i in range(3):  # create 3 units

        user_input = input('Please choose a profession for your unit("0" for Tanker,"1" for Warrior): ')

        if user_input == "1" or user_input == "0":
            type = int(user_input)
            pass
        else:
            type = random.randint(0, 1)
            input("Invalid input!! Random profession is created.\n " +
                  "===press ENTER to continue===")

        name = input('Please name your unit:')
        uid = i + 1
        attr.append((name, type, uid))
        units.append(UnitCreated(attr[i][0], attr[i][1], attr[i][2]))
        UnitCreated.print_attr(units[i])
    print("===player's team===")
    for i in range(len(units)):
        UnitCreated.print_attr(units[i])
    input("===Press ENTER to continue===")
    global en_units
    for i in range(3):
        en_type = random.randint(0, 1)
        en_name = "AI" + str(random.randint(10, 99))
        en_id = i + 1
        en_attr.append((en_name, en_type, en_id))
        en_units.append(UnitCreated(en_attr[i][0], en_attr[i][1], attr[i][2]))
    print("===enemy team===")
    for i in range(len(en_units)):
        UnitCreated.print_attr(en_units[i])

    uid_chosen = input("please choose your unit by enter his/her id :")


if __name__ == "__main__":
    main()
