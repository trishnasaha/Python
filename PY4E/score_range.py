sc = input("score:")
score = float(sc)
if score < 0.0 or score > 1.0:
    print("out of range")

elif score >= 0.9:
    print("grade A")
elif score >= 0.8:
    print("grade B")
elif score >= 0.7:
    print("grade C")
elif score >= 0.6:
    print("grade D")
elif score < 0.6:
    print("garde F")