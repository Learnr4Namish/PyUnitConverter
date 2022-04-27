import numpy as np

numeratorINP = input("Please enter the numerator of your rational number: \n")
denominatorINP = input("Please enter the denominator of your rational number \n")
try:
    numerator = int(int(numeratorINP))
    denominator = int(denominatorINP)
    gcdOfNAD = int(np.gcd(numerator, denominator))
    simpleNumerator = int(numerator/gcdOfNAD)
    simpleDenominator = int(denominator/gcdOfNAD)
    print("Your rational number in simplest form is " + str(simpleNumerator) + "/" + str(simpleDenominator))
except:
    print("Please provide an integer numerator or denominator.")