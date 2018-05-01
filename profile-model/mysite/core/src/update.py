import sys
from mysite.core.src.table import TABLE
from sys import argv


def update(new):
    sys.path.insert(0, "/home/pallabeedey/Xtras/profile-model/mysite/core/src")
    TABLE.update(new)
#    print (TABLE)
    with open ("/home/pallabeedey/Xtras/profile-model/mysite/core/src/table.py","w") as file:
        file.write("TABLE=")
        file.write(str(TABLE))
        file.close()
