import random
import sys

def risk_dice():
    a1 = random.randint(1,6)
    a2 = random.randint(1,6)
    a3 = random.randint(1,6)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print("Dice:")
    print(("  Attacker: {0}-{1}-{2}").format(a1,a2,a3))
    print(("  Defender: {0}-{1}").format(d1,d2))

risk_dice()
