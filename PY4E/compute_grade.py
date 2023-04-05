def computegrade(s):
    if s < 0.0 or s > 1.0:
        return("Bad score")
    elif s >= 0.9:
        return("A")
    elif s >= 0.8:
        return("B")
    elif s >= 0.7:
        return("C")
    elif s >= 0.6:
        return("D")
    elif s < 0.6:
        return("F")

sc = input("score:")
try:
    score = float(sc)
    grade = computegrade(score)
    print(grade)
except:
    print("Bad")
    quit()