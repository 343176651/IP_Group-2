import random
import re
from UnitCreated import UnitCreated
import time

units = []
en_units = []


class CheckUid:
    uid = 0

    @classmethod
    def checknum(cls, id_chosen):
        pattern = re.compile('^([1-3])$')
        if pattern.search(id_chosen) is not None:
            cls.uid = int(id_chosen)
            return print("ID({}) is selected".format(cls.uid))
        else:
            cls.uid = random.randint(1, 3)
            return print("Invalid ID, random ID({}) is selected".format(cls.uid))

    @classmethod
    def checkstr(cls, str):
        pattern2 = re.compile('^([y/n])$')
        if pattern2.search(str) is not None:
            return str
        else:
            print("Input Error!")
            inf_att = input("Do you want to attack the same target until a kill ?(y/n)")
            return inf_att


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

        # unit get exp
        units[uindex].set_exp(units[uindex].get_exp() + self.udamage)

        # damage enemy dealed
        self.edamage = self.eunit_atk - self.unit_def
        if self.edamage <= 0:
            self.edamage = 1

        # set unit health
        units[uindex].set_health(self.unit_health - self.edamage)

        # target get exp
        en_units[eindex].set_exp(en_units[eindex].get_exp() + self.edamage)


class AIAttack:
    def __init__(self):
        eid = random.randint(0,2)
        uid = random.randint(0,2)
        while True:
         if UnitCreated.state_check(units[eid]) == 1 and UnitCreated.state_check(en_units[uid]) == 1:
            Attack(eid, uid)
            UnitCreated.upgrade(units[uid])  # upgrade if possible
            UnitCreated.upgrade(en_units[eid])

            UnitCreated.print_attr(en_units[eid])
            UnitCreated.print_attr(units[uid])  # print state after attack
            break
        else:
            eid = random.randint(0,2)
            uid = random.randint(0,2)


def main():
    attr = []
    en_attr = []
    print("===Create your unit===")
    global units
    global en_units

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

    CheckUid.checknum(uid_chosen)  # check input

    uindex = CheckUid.uid - 1

    UnitCreated.print_attr(units[uindex])  # index of list = id - 1

    eid_chosen = input("please choose enemy unit you want to attack by enter his/her id :")

    CheckUid.checknum(eid_chosen)  # check input

    eindex = CheckUid.uid - 1

    UnitCreated.print_attr(en_units[eindex])

    Attack(uindex, eindex)

    print("===Attacking...===")
    time.sleep(1)  # simulate attacking

    UnitCreated.upgrade(units[uindex])  # upgrate if possible
    UnitCreated.upgrade(en_units[eindex])

    UnitCreated.print_attr(units[uindex])
    UnitCreated.print_attr(en_units[eindex])  # Print unit's state after attack

    print("===Attack finished===")

    print("===AI's turn===")
    time.sleep(1)
    print("===Attacking...===")
    time.sleep(2)  # simulate attacking

    en_uindex = random.randint(0, 2)
    en_eindex = random.randint(0, 2)

    # only attack when both alive
    AIAttack()
    print("===Attack finished===")
    time.sleep(1)
    # inf_att = input("Do you want to attack same target until a kill ?(y/n)")

    # result = CheckUid.checkstr(inf_att)  # Check input

    # if result == "n":
    #    pass
    # else:
    #    while en_units[eindex].get_health() > 0 and units[uindex].get_health() > 0:
    #        Attack(uindex, eindex)

    print("===player's team===")

    # print player's whole team
    for i in range(len(units)):
        UnitCreated.print_attr(units[i])
    time.sleep(1)
    print("===enemy team===")

    # print enemy team
    for i in range(len(en_units)):
        UnitCreated.print_attr(en_units[i])


if __name__ == "__main__":
    main()
