fname = input("enter a file name: ")

fhand = open(fname)

inp = fhand.read()

print(inp.upper())