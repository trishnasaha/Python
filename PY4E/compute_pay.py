def computepay(h, r):
    if h <= 40:
        p = h * r
    else:
        p = (h * r) + ((h - 40) * (r * 1.5))
    return p

inh = input("enter hours: ",)
hour = float(inh)
inr = input("enter rate: ",)
rate = float(inr)

pay = computepay(hour, rate)
print(pay)