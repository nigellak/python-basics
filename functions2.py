# convert length(m) to feet, cm, km

def length1 (m, FT=3.281):
    l = m * FT
    return l

print(length1(5))

def length2 (m, cm=100):
    j = m * cm
    return j

print(length2(5))

def length3 (m, km=1000):
    g = m * km
    return g

print(length3(5))