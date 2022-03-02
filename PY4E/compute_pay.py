def computepay(h, r):
    if hour <= 40:
        pay = hour * rate
    else:
        pay = (hour * rate) + ((hour - 40) * (rate * 1.5))
    return pay

inh = input("enter hours: ",)
hour = float(inh)
inr = input("enter rate: ",)
rate = float(inr)

pay = computepay(hour, rate)
print(pay)