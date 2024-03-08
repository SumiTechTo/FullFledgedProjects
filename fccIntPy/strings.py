mystr=" I'm Hello World"
print(mystr)

#  multiline string
mystr2="""Hello   
World"""
print(mystr2)


print(mystr2[0])
#H

#string are immutable

print(mystr2[0:5])
#Hello
#doesn't include the character in 5th position

# reversing string
mystr3=mystr2[::-1]
print(mystr3)

for i in mystr2:
    print (i)

if 'ell' in mystr2:
    print("yes")
else: print("No")

str= '   hello    '
print(str)

str=str.strip()
print(str)
#this changes the original string 
# but 
print(str.strip())
# doesn't


print(str.startswith('hello'))
# case sensitive

print(str.endswith('o'))

print(str.find('o'))
# if true- returns index 
# False - returns -1

print(str.count('l'))
# counts no.of given string present


print(str.replace('llo','rd'))
# creates andprints a new string

#and if the string to changed is not present it will just print the original string

