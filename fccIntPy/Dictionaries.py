mydict ={"name":"Max","age":28,"city":"NY"}
print (mydict)

mydict2=dict(name="Mary",age=27,city="Boston")
print (mydict2)

value= mydict ["name"]
print(value)
# //[prints value for the key]

#mutable
# if same key is used then value gets overwritten
mydict["email"]="gmail.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")

mydict.popitem() 
#deletes the last element
print(mydict)

mydict ={"name":"Max","age":28,"city":"NY"}
if "name" in mydict:
    print(mydict["city"])


try :
    print(mydict["name"])
except:
    print("Error")

for key in mydict:
    print(key) 
    #prints them in diff lines

for key in mydict.keys():
    print(key)
    #prints them in diff lines

for value in mydict.values():
    print(value)

for key,value in mydict.items():
    print(key,":",value)

mydict_cpy=mydict
print (mydict_cpy)

mydict_cpy["email"]="gmail.com"
print(mydict)
#modifies the original dictionary 

mydict_cpy=mydict.copy();
mydict_cpy["ph"]=9038
print(mydict_cpy)
print(mydict)

mydict.update(mydict_cpy)
#makes changes from mydicy_cpy to mydict\
#i.e changes everythingthat is different and adds newly found keys 

mytuple=(8,7)
mydict2={mytuple:"age"}
print(mydict2)

# alist cannot be used as a key  because they are mutable

 