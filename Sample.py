Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("Welcome to Assignment-1")
Welcome to Assignment-1
num1=10
>>> num2=30
>>> add=num1+num2
>>> print(add)
40
>>> print(num1)
10
>>> print("Num1= (num1)")
Num1= (num1)
>>> num1 = int(input("Num1 = "))
Num1 = 10
>>> num2 = int(input("Num2 = "))
Num2 = 30
>>> add = num1+num2
>>> print (Num1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print (Num1)
NameError: name 'Num1' is not defined. Did you mean: 'num1'?
>>> print (Num1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print (Num1)
NameError: name 'Num1' is not defined. Did you mean: 'num1'?
>>> print(Num1)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(Num1)
NameError: name 'Num1' is not defined. Did you mean: 'num1'?
>>> print (num1)
10
>>> print (num2)
30
>>> print ("Add = " add)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print ("Add = ", add)
Add =  40
>>> print ("Num1 = ", num1)
Num1 =  10
>>> print ("Num2 = ", num2)
Num2 =  30
