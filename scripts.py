#Problem 1
#Small note, I know these aren't many exercices but I just decided to enroll here, so this is what I was able to do in two days. Hope I can make it up with the other homeworks.
#-------Challenge 1 - Introduction

#1) Hello World
print("Hello, World")

#2)If Else 
def test_weird(n):
    if (n%2) ==1 :
        print ("Weird")
    elif (n>=2 and n<=5):
        print ("Not Weird")
    elif (n>=6 and n<=20 ):
        print ("Weird")
    elif n>20 : 
        print ("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())

test_weird(n)

#3) Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

def operations(a,b):
    print (a+b)
    print (a-b)
    print (a*b)

operations(a,b)

#4) Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

def operations(a,b):
    print (a+b)
    print (a-b)
    print (a*b)

operations(a,b)

#5) Loops 
if __name__ == '__main__':
    n = int(input())

def loop(n):
    for i in range(n):
        print(i**2)

loop(n)

#6) Write a function
def is_leap(year):
    leap = False
    
    if ((year%4) == 0 and not (year%100)==0) or (year%400) == 0 :
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#7) Print Function
if __name__ == '__main__':
    n = int(input())

def printline(n):
    for i in range(1,n+1):
        print(i, end='')

printline(n)


#-------Challenge 2 - Data Types

#1) List Comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

print [ [ i, j, k] for i in range( x +1 ) for j in range( y + 1) for k in range( z+ 1) if ( ( i + j + k) != n )]

#2)Find the runner-up score

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

def runnerup(arr):
    lista = list(arr)
    lista = list( dict.fromkeys(lista) )
    lista.remove(max(lista))
    print max(lista)

runnerup(arr) 

#3) Nested List
biglist=[]

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    a= [name,score]
    biglist.append(a)


min = biglist[0][1]
for l in biglist:
    if l[1] < min:
        min = l[1]


newlist= []
for l in biglist:
    if l[1] != min:
        newlist.append(l)

newlist = sorted(newlist, key = lambda x: x[1])

value = newlist[0][1]
stud = []
for l in newlist:
    if l[1] == value:
        stud.append(l[0])

stud.sort()
for p in stud: print p 

#4) Finding percentage 

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    voti = student_marks[query_name]
    res = round( sum(voti)/3,2)
    final = format(res, '.2f')
    print final 

 #5)Lists 

l =[]
if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        command = input()
        if "insert" in command: 
            #print(command)
            lista = command.split(" ")
            l.insert(int(lista[1]), int(lista[2]))
        if "print" in command:
            print(l)
        if "remove" in command:    
            lista = command.split(" ")
            l.remove(int(lista[1]))
        if "append" in command: 
            lista = command.split(" ")
            l.append(int(lista[1]))
        if "sort" in command:
            l.sort()
        if "pop" in command:
            l.pop()
        if "reverse" in command:
            l.reverse()

#6) Tuples

l = []
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    for i in integer_list:
        l.append(i)

t = tuple(l)
print(hash(t))


#-------Challenge 3 - Strings

#1) SwapCase
def swap_case(s):
    sw = s.swapcase()
    return sw 

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#2) Split & Join 

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line 

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result


#3) What's your name?
def print_full_name(a, b):
    print "Hello " + a +" " + b + "! You just delved into python."

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)

#4) Mutation 
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string 

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

#5) Find a string 

def count_substring(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count

#6) String Validators 
alnum = False
alpha = False
digit = False
lower = False
upper = False

if __name__ == '__main__':
    s = raw_input()
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True 
        
        if i.isdigit():
            digit = True 
        
        if i.islower():
            lower = True 
        
        if i.isupper():
            upper = True 

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)

#7)Text alignement 
thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)

#8) Text Wrap
import textwrap


def wrap(string, max_width):
import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width) 
    lista = wrapper.wrap(text=string) 
    return "\n".join(lista)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



#9) Designer Door Mat

#10) String Formatting 

def print_formatted(number):
    binN = "{0:b}".format(number)
    lun = len(binN)
    for i in range(1,number+1):
            octal = "{0:o}".format(i)
            hexa =  "{0:x}".format(i).upper()
            binar = "{0:b}".format(i)
            line_new = '{i:>{max_width}} {octal:>{max_width}} {hexa:>{max_width}} {binar:>{max_width}}'.format(max_width = lun, i = i, octal = octal, hexa = hexa, binar=  binar)
            print(line_new)


#11) Alphabet Rangoli

#12) Capitalize 

n = [ ]
def solve(s):
    l = s.split(" ")
    for e in l: 
        e = e.capitalize()
        n.append(e)
    res = " ".join(n)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#-------Challenge 4 - Sets

#1) Introduction to Sets

def average(array):
    s = set(array)
    return sum(s)/len(s) 

#2) Simmetric Difference 


M = int(input())
mlist = input().split(" ")
mset = set(mlist)
N = int(input())
nlist = input().split(" ")
nset = set(nlist)

res = []
first = mset.difference(nset)
second = nset.difference(mset)
for e in first:
    res.append(e)
for e in second:
    res.append(e)

res = [int(x) for x in res]
res.sort()

for e in res:
    print(e)

#3) Set.add()


tot = int(input())
sett = set()
for i in range(tot):
    sett.add(input())

print(len(sett))

#4) set.discard(), .remove(), .pop()

n = int(input())
s = set(map(int, input().split()))

ncom = int(input())

for i in range(ncom):
        command = input()
        if "pop" in command: 
            s.pop()
        if "remove" in command:
            lista = command.split(" ")
            s.remove(int(lista[1]))
        if "discard" in command: 
            lista = command.split(" ")
            s.discard(int(lista[1]))

print(sum(s))

#5) set.union() Operation

en = int(input())
eset = set(map(int, input().split()))

fn = int(input())
fset = set(map(int, input().split())) 

fonly = fset.difference(eset)
print (len(fonly)+ len(eset))

#6) Set.intersection() Operation

en = int(input())
eset = set(map(int, input().split()))

fn = int(input())
fset = set(map(int, input().split())) 

both = fset.intersection(eset)
print(len(both))

#7) Set.difference() Operation

en = int(input())
eset = set(map(int, input().split()))

fn = int(input())
fset = set(map(int, input().split())) 

eonly = eset.difference(fset)
print (len(eonly))

#8) Set.symmetric_difference() Operation

en = int(input())
eset = set(map(int, input().split()))

fn = int(input())
fset = set(map(int, input().split())) 

symdiff = eset.symmetric_difference(fset)
print (len(symdiff))

#9) Set Mutations (only 2 tests ok, EOF problem with input)
n = int(input())
#print(n)
s = set(map(int, input().split()))
    

ncom = int(input())

for i in range(ncom):
        command = input()
        newset = set(map(int, input().split()))
        if "intersection_update" in command: 
            s.intersection_update(newset)
        if "update" in command and "intersection" not in command:
            s.update(newset)
        if "symmetric_difference_update" in command: 
            s.symmetric_difference_update(newset)
        if "difference_update" in command:
            s.difference_update(newset)

print (sum(s))

#10) The captain's Room 

#11) Check Subset 

n = int(input())

for i in range(n):
    mainl = int(input())
    main = set(map(int, input().split()))
    testl = int(input())
    test = set(map(int, input().split()))
    if main.issubset(test):
        print("True")
    else: 
        print("False")

#12) Check Strict Superset 

bigset = set(map(int, input().split()))
n = int(input())
flag = False

for i in range(n):
    
    test = set(map(int, input().split()))
    if test.issubset(bigset) and len(bigset)> len(test):
        flag = True 
    else: 
        flag = False
        break;

print(flag) 


#13) No idea

lineone = input().split()
n = int(lineone[0])
m = int(lineone[1])

array = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

happ = 0
for i in array:
    if i in A:
        happ+=1
for i in array:
    if i in B:
        happ-=1

print(happ)


#------Challenge 5 - Collections 

#------Challenge 6 - Date & Time 

#1) Calendar Module
import calendar
diz = { 0 : "MONDAY", 1 : "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}
string = input()
info = string.split(" ")
#print(info[2], info[1], info[0])
d = calendar.weekday(int(info[2]), int(info[0]), int(info[1]))

print(diz.get(d))

#2) Time Delta 
import math
import os
import random
import re
import sys

from datetime import datetime
fmt = "%a %d %b %Y %H:%M:%S %z"
# Complete the time_delta function below.
def time_delta(t1, t2):
    first = datetime.strptime(t1, fmt)
    second = datetime.strptime(t2, fmt)
    sec = (first-second).total_seconds() 
    return str(int(abs(sec)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



#------Challenge 7 - Exceptions

#1) Exceptions
r = int(input())
#print(r)
for i in range(r):
    line = input().split(" ")
    a = line[0]
    b = line[1]
    try: 
        a = int(a)
        b = int(b)
        try: print(a//b)
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

#------Challenge 8 - Built-ins

#1) Zipped

line = input().split()
stun = int(line[0])
subn = int(line[1])

info = []

for i in range(subn):
    info.append(list(map(float, input().split())))

for i in zip(*info):
    print( sum(i)/subn)

#2) Athlete Sort
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key = lambda x: x[k]) 
    
    for i in arr:
        i = [str(x) for x in i]
        print(" ".join(i))

#3) ginortS

string = input()
low =[]
upp = []
even = []
odd = []

for i in string:
    if i.isalpha():
        if i.islower():
            low.append(i)
        else:
            upp.append(i)
    if i.isdigit():
        if int(i)%2 == 0:
            even.append(i)
        else: 
            odd.append(i)

low.sort()
upp.sort()
even.sort()
odd.sort()

print("".join(low)+"".join(upp)+"".join(odd)+"".join(even))

#---------Challenge 9 - Python Functionals 

#1) Map and Lambda Function 

cube = lambda x: (x*x*x) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    res = []
    for i in range (n):
        if i == 0 or i==1:
            res.append(i)
        else: 
            res.append(res[i-1]+res[i-2])
    return res 

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#--------Challenge 13 - Numpy

#1) Arrays 

import numpy

def arrays(arr):
    arr.reverse()
    res = numpy.array(arr, float)
    return res 

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


















