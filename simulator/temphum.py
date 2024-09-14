#!/usr/bin/env python3

import random

def temperature() -> float:
    if random.binomialvariate(1, 0.01) >= 1:
        return round(75 + random.normalvariate(0, 10), 2)
    return round(35 + random.normalvariate(0, 5), 2)

def humidity():
    if random.binomialvariate(1, 0.05) >= 1:
        return round(70 + random.normalvariate(0, 10), 2)
    return round(30 + random.normalvariate(0, 5), 2)

if __name__ == "__main__":
    c = temperature()
    f = round(c * 1.8 + 32, 2)
    print(f"Bus 001 Dev 012 3553:a001 TEMPerHUM_V4.1 {c}C {f}F {humidity()}% - - -")