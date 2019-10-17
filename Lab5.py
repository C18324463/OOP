from math import gcd

frac1 = 57, 12
frac2 = 68, 39

def gcd(big, small):
    if big < small:
        big, small = small, big
    if small == 0:
        return big
    return  gcd(small,  big % small)

print("GCD of 12 and 57 is " + str(gcd(frac1[0], frac1[1])))

def lcm(first, second):
    LCM = (first * second) / gcd(first, second)
    return LCM

print("LCM of 57 and 12 is", str(lcm(frac1[0], frac1[1])))

def addfrac(frac1, frac2):
    denominator = lcm (frac1[1], frac2[1])
    numerator = (frac1[0] * (denominator / frac1[1])) + (frac2[0] * (denominator / frac2[1]))

    FractionReturn = numerator, denominator

    return FractionReturn

fraction_answer1 = addfrac(frac1, frac2)
print("Frac1 plus Frac2 equals", str(fraction_answer1[0] , "/" , fraction_answer1[1]))
