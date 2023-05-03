#Use find and string slicing to extract the portion of the string after the colon character and 
#then use the float function to convert the extracted string into a floating point number.


str = 'X-DSPAM-Confidence:0.8475'

semicolpos = str.find(':')

print(semicolpos)

numpos = str[semicolpos+1:]

print(numpos)

fpos = float(numpos)

print(fpos)