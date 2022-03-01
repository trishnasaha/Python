inh = input("enter hours: ",)
hour = float(inh)
inr = input("enter rate: ",)
rate = float(inr)
if hour <= 40 :
    pay = hour * rate
    print ("regular", pay)
else:
    pay = (hour * rate) + ((hour - 40) * (rate * 1.5))

print ("overtime", pay)