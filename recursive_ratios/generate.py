import operator
from random import random, randint
import math

operators_strs = {
    0: "+",
    1: "-",
    2: "*",
    3: "/"
}

operators = {
    0: operator.add,
    1: operator.sub,
    2: operator.mul,
    3: operator.truediv
}

def getCoef(selection):
    if selection < 3:
        return randint(0,100)
    else:
        return random()

origA1 = a1 = randint(0,100)
origA2 = a2 = randint(0,100)
a1Selection = randint(0,3)
a2Selection = randint(0,3)
a1CoefOp = operators[a1Selection]
a2CoefOp = operators[a2Selection]
a1Coef = getCoef(a1Selection)
a2Coef = getCoef(a2Selection)
majorOppSelection = randint(0,1)
majorOpp = operators[randint(0,1)]
ratio = 0

for i in range(0,1000):
    a3 = majorOpp(a1CoefOp(a1,a1Coef), a2CoefOp(a2,a2Coef))
    if abs(ratio-a3/a2) < .00001:
        print("a1 = %d" % origA1)
        print("a2 = %d" % origA2)
        print("a[n+1] = (%f %s a[n-1])%s(%f %s a[n]) ---> %f" % (a1Coef, operators_strs[a1Selection], operators_strs[majorOppSelection], a2Coef, operators_strs[a2Selection], ratio))
        break
    ratio = a3/a2
    print(ratio)
    a1 = a2
    a2 = a3
