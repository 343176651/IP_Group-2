import random
import re
import UnitCreated

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

    UnitCreated.print_attr(units[int(uid_chosen - 1)])  # index of list = id - 1

    eid_chosen = input("please choose enemy unit you want to attack by enter his/her id :")

    CheckUid.check(eid_chosen)

    UnitCreated.print_attr(units[int(eid_chosen - 1)])


if __name__ == "__main__":
    main()
