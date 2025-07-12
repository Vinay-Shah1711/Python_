# String Methods
# Strings immutable it means not changeable

a="!!Vinay!! !!!!!!!!! Vinay!"
print(len(a))
print(a)
print(a.upper())

print(a.lower())

print(a.rstrip("!"))

print(a.replace("Vinay","Shah"))

print(a.split(" "))

bloghead="introduction to jS"
print(bloghead.capitalize())

str1="This is best "
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

print(a.count("Vinay"))

str2 = "Welcome to the Console !!!"
print(str2.endswith("!!!"))

str2 = "Welcome to the Console !!!"
print(str2.endswith("to", 4, 10))

str3="My name is vinay shah"
print(str3.find("is"))
print(str3.find("ishh"))

print(str3.index("is"))

str4="Welcomeinpython1"
print(str4.isalnum())

str4="Welcomeinpython1"
print(str4.isalpha())
str4="Welcomeinpython"
print(str4.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1)
print(str1.isprintable())

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = ""       #using Tab
print(str2.isspace())

str1="My Name Is Vinay"
print(str1.istitle())

str1="MY NAME IS VINAY"
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language, but Easy Language" 
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())