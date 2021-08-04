import random


class UnitCreate:
    name = ""
    health = 100
    experience = 0
    rank = 1
    attack = 0
    defence = 0
    type = 0  # 0 = tanker 1 = warrior
    profession = ""

    def __init__(self, name, type):
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
        print("NAME: {},profession: {},HP: {},EXP: {},RANK: {},ATK: {},DEF: {}"
              .format(self.name, self.profession, self.health, self.experience,
                      self.rank, self.attack, self.defence))


def main():
    print("===Create your unit===")
    units = []
    attr = []
    en_units = []
    en_attr = []
    for i in range(3):
        type = int(input('Please choose a profession for your unit("0" for Tanker,"1" for Warrior): '))
        name = input('Please name your unit:')
        attr.append((name, type))
        units.append(UnitCreate(attr[i][0], attr[i][1]))
    print("===player's team===")
    for i in range(len(units)):
        UnitCreate.print_attr(units[i])
    input("===Press enter to continue===")

    for i in range(3):
        en_type = random.randint(0, 1)
        en_name = "AI" + str(random.randint(10, 99))
        en_attr.append((en_name, en_type))
        en_units.append(UnitCreate(en_attr[i][0], en_attr[i][1]))
    print("===enemy team===")
    for i in range(len(en_units)):
        UnitCreate.print_attr(en_units[i])


main()
