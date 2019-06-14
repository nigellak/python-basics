# convert ksh to ugsh or tzsh or usd(default)
# ksh = kenyan shillings
# tsh = tanzanian shillings
# ugx = ugandan shillings
# usd = us dollar

# ksh = input('enter amount in ksh')
# ksh = float(ksh)
# ugx = input('enter amount in ugx')
# ugx = int(ugx)

# rates ={'ksh''ugx': 36.96, 'ksh''tsh': 22.64, 'ksh''usd':0.0099 }
#
# def currencyconverter1(ksh, ugx):
#     amount = 0
#     for  ksh in range (0, 1000000):
#       rates()

    # , tsh, usd = 0.0099):
    # # elif amount in tsh:
    # amount = ksh * 22.64
    # print(amount)
    #
    # # elif amount in usd:
    # amount = ksh * usd
    # print(amount)
    #



def currencyconverter1(ksh, ugx=36.81):
    c = ksh * ugx
    return c

print(currencyconverter1(300))


def currencyconverter2(ksh,tsh=22.64):
    c = ksh * tsh
    return c

print(currencyconverter2(500))


def currencyconverter3(ksh, usd=0.0098):
    c = ksh * usd
    return c

print(currencyconverter3(65000))



