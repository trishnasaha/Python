inh = input("enter hours: ",)
inr = input("enter rate: ",)
try:
    hour = float(inh)
    rate = float(inr)
except:
    print("type a number")
    quit()

print (hour, rate)
if hour <= 40 :
    pay = hour * rate
else:
    pay = (hour * rate) + ((hour - 40) * (rate * 1.5))

print (pay)