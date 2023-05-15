def duplicate_list(std: list):
    for i in std:
        if std.count(i) > 1:
            print(f"the item {i} occurred more than once")
        else:
            print(f"there's no duplicate")


y_list = ["pen", "pet", "ken", "pep", "pen"]


    