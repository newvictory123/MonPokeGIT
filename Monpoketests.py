import random



def Health(Base):
        finalHP= ((((2 * Base + random.randint(1,31) + (85/4))*50)/100)+10+50)
        return finalHP
        print(finalHP)

def Otherstat(stat):
        finalstat = ((((2*stat) + random.randint(0, 31) +(85/4))*50/100)+5)
        return finalstat
        print(finalstat)

def Healthtest(base):
    if ((((2 * base + 1 + (85/4))*50)/100)+10+50) <= Health(base) <= ((((2 * base + 31 + (85/4))*50)/100)+10+50):
        print("succes")
    else:
        print("failure")

def otherstattest(base):
    if ((((2*base) + 1 +(85/4))*50/100)+5) <= Otherstat(base) <= ((((2*base) + 31 +(85/4))*50/100)+5):
        print("succes")
    else:
        print("failure")

Healthtest(40)

otherstattest(40)
