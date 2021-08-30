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

    # @classmethod
    # def checkstr(cls, str):
    #     pattern2 = re.compile('^([y/n])$')
    #     if pattern2.search(str) is not None:
    #         return str
    #     else:
    #         print("Input Error!")
    #         inf_att = input("Do you want to attack the same target until a kill ?(y/n)")
    #         return inf_att


class Attack:
    def __init__(self, uindex, eindex):
        global units
        global en_units
        time.sleep(1)
        print("===Attacking...===")
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

        # when health below 0 set to 0
        if en_units[eindex].get_health() < 0:
            en_units[eindex].set_health(0)

        # unit get exp
        units[uindex].set_exp(units[uindex].get_exp() + self.udamage)

        # damage enemy dealed
        self.edamage = self.eunit_atk - self.unit_def
        if self.edamage <= 0:
            self.edamage = 1

        # set unit health
        units[uindex].set_health(self.unit_health - self.edamage)

        # when health below 0 set to 0
        if units[uindex].get_health() < 0:
            units[uindex].set_health(0)

        # target get exp
        en_units[eindex].set_exp(en_units[eindex].get_exp() + self.edamage)

        # print attr after attack
        time.sleep(1)
        UnitCreated.print_attr(units[uindex])
        UnitCreated.print_attr(en_units[eindex])
        print("===Attack finished===\n")


def aiAttack():
    while True:
        eid = random.randint(0, 2)
        uid = random.randint(0, 2)
        # only attack when both alive
        if UnitCreated.state_check(units[uid]) == 1 and UnitCreated.state_check(en_units[eid]) == 1:
            Attack(uid, eid)
            UnitCreated.upgrade(units[uid])  # upgrade if possible
            UnitCreated.upgrade(en_units[eid])
            break
        else:
            break


def checkField():
    ustate = 0
    estate = 0
    for i in range(len(units)):
        if UnitCreated.state_check(units[i]) == 1:
            ustate = ustate + 1
    if ustate == 0:
        print("Game Over! You lost!")
        return 0
    else:
        for i in range(len(en_units)):
            if UnitCreated.state_check(en_units[i]) == 1:
                estate = estate + 1
        if estate == 0:
            print("Congratulation! You Won!")
            return 1


def main():
    attr = []
    en_attr = []
    will = 1
    print("===Create your unit===")
    global units
    global en_units

    # create player's units
    for i in range(3):

        user_input = input('\nPlease choose a profession for your unit("0" for Tanker,"1" for Warrior): ')

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

    print("\n===player's team===")

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

    print("\n===enemy team===")

    # print enemy team
    for i in range(len(en_units)):
        UnitCreated.print_attr(en_units[i])
    input("===Press ENTER to continue===")
    # Loop start
    while checkField() is None:

        uid_chosen = input("\nplease choose your unit by enter his/her id :")

        CheckUid.checknum(uid_chosen)  # check input

        uindex = CheckUid.uid - 1  # index of list = id - 1

        UnitCreated.print_attr(units[uindex])

        eid_chosen = input("\nplease choose enemy unit you want to attack by enter his/her id :")

        CheckUid.checknum(eid_chosen)  # check input

        eindex = CheckUid.uid - 1

        UnitCreated.print_attr(en_units[eindex])
        print("\n")
        Attack(uindex, eindex)
        time.sleep(1)  # simulate attacking

        UnitCreated.upgrade(units[uindex])  # upgrate if possible
        UnitCreated.upgrade(en_units[eindex])

        ###
        # UnitCreated.print_attr(units[uindex])
        # UnitCreated.print_attr(en_units[eindex])  # Print unit's state after attack
        ###

        time.sleep(2)
        print("===AI's turn===")
        time.sleep(1)


        aiAttack()
        time.sleep(1)

        print("\n===player's team===")

        # print player's whole team
        for i in range(len(units)):
            UnitCreated.print_attr(units[i])
        time.sleep(1)
        print("\n===enemy team===")

        # print enemy team
        for i in range(len(en_units)):
            UnitCreated.print_attr(en_units[i])

        if checkField() is not None:  # when one of the teams all dead
            # print player's whole team
            print("\n===player's team===")
            for i in range(len(units)):
                UnitCreated.print_attr(units[i])

            # print enemy team
            print("\n===enemy team===")
            for i in range(len(en_units)):
                UnitCreated.print_attr(en_units[i])
            break

        if will == 1:
            auto = input("\nDo you want to turn on the auto attack? (y/n)")
        if auto == "y":
            while checkField() is None:  # when both team have units alive
                aiAttack()
            # print player's whole team
            print("\n===player's team===")
            for i in range(len(units)):
                UnitCreated.print_attr(units[i])

            # print enemy team
            print("\n===enemy team===")
            for i in range(len(en_units)):
                UnitCreated.print_attr(en_units[i])
        else:
            will = 0


if __name__ == "__main__":
    main()
