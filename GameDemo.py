import random
import re
from UnitCreated import UnitCreated

units = []
en_units = []


class CheckUid:
    uid = 0

    @classmethod
    def check(cls, id_chosen):
        pattern = re.compile('^([1-3])$')
        if pattern.search(id_chosen) is not None:
            cls.uid = int(id_chosen)
            return print("ID({}) is selected".format(cls.uid))
        else:
            cls.uid = random.randint(1, 3)
            return print("Invalid ID, random ID({}) is selected".format(cls.uid))

class Attack:
    def __init__(self, uindex, eindex):
        global units
        global en_units

        # unit's attribute
        self.unit_health = units[uindex].get_health()
        self.unit_atk = units[uindex].get_atk()
        self.unit_def = units[uindex].get_def()

        # enemy attribute
        self.eunit_health = en_units[eindex].get_health()
        self.eunit_atk = en_units[eindex].get_atk()
        self.eunit_def = en_units[eindex].get_def()

        # damage unit dealed
        self.udamage = self.unit_atk - self.eunit_def
        if self.udamage <= 0:
            self.udamage = 1

        # set enemy health
        en_units[eindex].set_health(self.eunit_health - self.udamage)

        # damage enemy dealed
        self.edamage = self.eunit_atk - self.unit_def
        if self.edamage <= 0:
            self.edamage = 1

        # set unit health
        units[uindex].set_health(self.unit_health - self.edamage)





def main():
    attr = []
    en_attr = []
    print("===Create your unit===")
    global units

    # create player's units
    for i in range(3):

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

        # show unit's attribute
        UnitCreated.print_attr(units[i])

    print("===player's team===")

    # print player's whole team
    for i in range(len(units)):
        UnitCreated.print_attr(units[i])

    input("===Press ENTER to continue===")
    global en_units

    # create enemy team
    for i in range(3):
        en_type = random.randint(0, 1)
        en_name = "AI" + str(random.randint(10, 99))
        en_id = i + 1
        en_attr.append((en_name, en_type, en_id))
        en_units.append(UnitCreated(en_attr[i][0], en_attr[i][1], attr[i][2]))

    print("===enemy team===")

    # print enemy team
    for i in range(len(en_units)):
        UnitCreated.print_attr(en_units[i])

    input("===Press ENTER to continue===")

    uid_chosen = input("please choose your unit by enter his/her id :")

    CheckUid.check(uid_chosen)  # check input

    uindex = CheckUid.uid - 1

    UnitCreated.print_attr(units[uindex])  # index of list = id - 1

    eid_chosen = input("please choose enemy unit you want to attack by enter his/her id :")

    CheckUid.check(eid_chosen)

    eindex = CheckUid.uid - 1

    UnitCreated.print_attr(en_units[int(eindex)])

    Attack(uindex,eindex)

    print("===Attack finished===")

    UnitCreated.print_attr(units[uindex])
    UnitCreated.print_attr(en_units[eindex])


if __name__ == "__main__":
    main()
