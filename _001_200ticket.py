
# generate 200 ticket
# 2016-5-8 00:50
import uuid


def get_ticket():
    return uuid.uuid1()


for x in range(1, 201):
    print(str(x)+" : "+get_ticket().__str__())
print(get_ticket().__str__().__len__())



