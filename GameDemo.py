import random
import re
import time
import sys
from UnitCreated import UnitCreated
from datetime import datetime

units = []
en_units = []


class Logger(object):
    def __init__(self, filename='eventLog.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger(stream=sys.stdout)


class CheckUid:
    uid = 0
    @classmethod
    def checknum(cls, id_chosen):
        pattern = re.compile('^([1-{}])$'.format(len(units)))
        if pattern.search(id_chosen) is not None:
            cls.uid = int(id_chosen)
            return print(datetime.now().strftime("%m-%d %H:%M:%S"), "ID({}) is selected".format(cls.uid))
        else:
            cls.uid = random.randint(1, len(units))
            return print(datetime.now().strftime("%m-%d %H:%M:%S"),
                         "Invalid ID, random ID({}) is selected".format(cls.uid))


class Attack:
    def __init__(self, uindex, eindex):
        global units
        global en_units
        time.sleep(0.5)
        print(datetime.now().strftime("%m-%d %H:%M:%S"), "===Attacking...===")
        # unit's attribute
        self.unit_health = units[uindex].get_health()
        self.unit_atk = units[uindex].get_atk()
        self.unit_def = units[uindex].get_def()

        # enemy attribute
        self.eunit_health = en_units[eindex].get_health()
        self.eunit_atk = en_units[eindex].get_atk()
        self.eunit_def = en_units[eindex].get_def()

        # damage unit dealed
        self.udamage = self.unit_atk - self.eunit_def + random.randint(0, 5)
        if self.udamage <= 0:
            self.udamage = 1 + random.randint(0, 5)

        # set enemy health
        en_units[eindex].set_health(self.eunit_health - self.udamage)

        # when health below 0 set to 0
        if en_units[eindex].get_health() < 0:
            en_units[eindex].set_health(0)

        # unit get exp
        units[uindex].set_exp(units[uindex].get_exp() + self.udamage * 2)

        # damage enemy dealed
        self.edamage = self.eunit_atk - self.unit_def + random.randint(0, 5)
        if self.edamage <= 0:
            self.edamage = 1 + random.randint(0, 5)

        # set unit health
        units[uindex].set_health(self.unit_health - self.edamage)

        # when health below 0 set to 0
        if units[uindex].get_health() < 0:
            units[uindex].set_health(0)

        # target get exp
        en_units[eindex].set_exp(en_units[eindex].get_exp() + self.edamage * 2)

        UnitCreated.upgrade(units[uindex])  # upgrade if possible
        UnitCreated.upgrade(en_units[eindex])
        # print attr after attack
        time.sleep(0.5)
        UnitCreated.print_attr(units[uindex])
        UnitCreated.print_attr(en_units[eindex])
        print("{} dealt {} damage to {}"
              .format(units[uindex].get_name(), self.udamage, en_units[eindex].get_name()))
        print("{} dealt {} damage to {}"
              .format(en_units[eindex].get_name(), self.edamage, units[uindex].get_name()))
        print(datetime.now().strftime("%m-%d %H:%M:%S"), "===Attack finished===\n")


def aiAttack():
    while True:
        eid = random.randint(0, len(en_units)-1)
        uid = random.randint(0, len(units)-1)
        # only attack when both alive
        if UnitCreated.state_check(units[uid]) == 1 and UnitCreated.state_check(en_units[eid]) == 1:
            Attack(uid, eid)
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
        print(datetime.now().strftime("%m-%d %H:%M:%S"), "Game Over! You lost!")
        return 0
    else:
        for i in range(len(en_units)):
            if UnitCreated.state_check(en_units[i]) == 1:
                estate = estate + 1
        if estate == 0:
            print(datetime.now().strftime("%m-%d %H:%M:%S"), "Congratulation! You Won!")
            return 1


def main():
    print(datetime.now().strftime("%m-%d %H:%M:%S"), "======================Game started======================")
    attr = []
    en_attr = []
    will = 1
    size = int(input("Please enter your team size(maximum at 9):\n"))
    print(datetime.now().strftime("%m-%d %H:%M:%S"), "===Create your unit===")
    global units
    global en_units

    # create player's units
    for i in range(size):

        user_input = input('\nPlease choose a profession for your unit("0" for Tanker,"1" for Warrior):\n ')

        if user_input == "1" or user_input == "0":
            type = int(user_input)
            pass
        else:
            type = random.randint(0, 1)
            input("Invalid input!! Random profession is created.\n " +
                  "===press ENTER to continue===")

        name = input('Please name your unit:\n')
        uid = i + 1
        attr.append((name, type, uid))
        units.append(UnitCreated(attr[i][0], attr[i][1], attr[i][2]))

        # show unit's attribute
        UnitCreated.print_attr(units[i])

    print(datetime.now().strftime("%m-%d %H:%M:%S"), "\n===player's team===")

    # print player's whole team
    for i in range(len(units)):
        UnitCreated.print_attr(units[i])

    input("===Press ENTER to continue===\n")

    # create enemy team
    for i in range(size):
        en_type = random.randint(0, 1)
        en_name = "AI" + str(random.randint(10, 99))
        en_id = i + 1
        en_attr.append((en_name, en_type, en_id))
        en_units.append(UnitCreated(en_attr[i][0], en_attr[i][1], attr[i][2]))

    print(datetime.now().strftime("%m-%d %H:%M:%S"), "\n===enemy team===")

    # print enemy team
    for i in range(len(en_units)):
        UnitCreated.print_attr(en_units[i])
    input("===Press ENTER to continue===")
    # Loop start
    while checkField() is None:
        while True:
            uid_chosen = input("\nplease choose your unit by enter his/her id :\n")

            CheckUid.checknum(uid_chosen)  # check input

            uindex = CheckUid.uid - 1  # index of list = id - 1

            UnitCreated.print_attr(units[uindex])

            eid_chosen = input("\nplease choose enemy unit you want to attack by enter his/her id :\n")

            CheckUid.checknum(eid_chosen)  # check input

            eindex = CheckUid.uid - 1

            UnitCreated.print_attr(en_units[eindex])
            print("\n")
            # only attack when both alive
            if UnitCreated.state_check(units[uindex]) == 1 and UnitCreated.state_check(en_units[eindex]) == 1:
                Attack(uindex, eindex)
                break
            else:
                print("Invalid attack! Please check the states of both unit.\n")
                pass

        time.sleep(1)

        if checkField() is None:  # when both team have units alive
            print(datetime.now().strftime("%m-%d %H:%M:%S"), "===AI's turn===")
            time.sleep(1)
            aiAttack()
            time.sleep(1)
            print('\n', datetime.now().strftime("%m-%d %H:%M:%S"), "===player's team===")

            # print player's team
            for i in range(len(units)):
                UnitCreated.print_attr(units[i])
            time.sleep(1)
            print('\n', datetime.now().strftime("%m-%d %H:%M:%S"), "===enemy team===")

            # print enemy team
            for i in range(len(en_units)):
                UnitCreated.print_attr(en_units[i])

        if checkField() is not None:  # when one of the teams is wiped
            # print player's whole team
            print('\n', datetime.now().strftime("%m-%d %H:%M:%S"), "===player's team===")
            for i in range(len(units)):
                UnitCreated.print_attr(units[i])

            # print enemy team
            print('\n', datetime.now().strftime("%m-%d %H:%M:%S"), "===enemy team===")
            for i in range(len(en_units)):
                UnitCreated.print_attr(en_units[i])
            break

        if will == 1:
            while True:
                auto = input("\nDo you want to turn on the auto attack? (y/n)\n")
                if auto == "y":
                    will = 0
                    while checkField() is None:  # when both team have units alive
                        aiAttack()
                    # print player's whole team
                    print('\n', datetime.now().strftime("%m-%d %H:%M:%S"), "===player's team===")
                    for i in range(len(units)):
                        UnitCreated.print_attr(units[i])

                    # print enemy team
                    print('\n', datetime.now().strftime("%m-%d %H:%M:%S"), "===enemy team===")
                    for i in range(len(en_units)):
                        UnitCreated.print_attr(en_units[i])

                    break
                elif auto == "n":
                    will = 0
                    break
                else:
                    print("Invalid Input!")
                    continue


if __name__ == "__main__":
    main()
