import ray

ray.init()

def currencyconverter1(ksh, ugx=36.81):
    c = ksh * ugx
    return c

@ray.remote
print(currencyconverter1(300))

def currencyconverter2(ksh,tsh=22.64):
    c = ksh * tsh
    return

@ray.remote
print(currencyconverter2(500))


def currencyconverter3(ksh, usd=0.0098):
    c = ksh * usd
    return c

@ray.remote
print(currencyconverter3(65000))
