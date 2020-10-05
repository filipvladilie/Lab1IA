# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import os

#tutoria 2
listEx = ['Vlad' , 21 , 'Bacau']
print listEx
listEx2 = [1,2,3,4,5]
listEx3 = ['z','a','w','y','t','c','x','q',]
listEx2[1] = 0
print listEx2
del listEx2[0]
print listEx2
listEx.append('Sef')
print listEx
listEx.remove('Bacau')
print listEx
listEx2.insert(2,0)
print listEx2
print listEx3
listEx3.sort()
print listEx3

print "\n"

#tutorial 3
dictEx =({"Name" : "Vlad", "Age": 21,"Height":184 })
print dictEx
print dictEx.get("Age")
print dictEx.items()
print dictEx.values()
dictEx.pop('Name')
print dictEx
name ='Vlad'
age = 21
charSex = 'M'
intkids = 0
married = False

print '%s is %f years old' %(name,age)
print 'Sex: %c' %(charSex)
print 'He has %d kids and said it\'s %s is married' %(intkids,married)

print "\n"
print '%.15f' %(math.pi)
print '%20f' %(math.pi)
bigString = 'Ana are mere si mai are si banane'
print bigString
print bigString.find('mai')
print bigString.count('a')
print bigString.count('a',3,25)
print bigString.upper()
print "\n"

#tutorial 4
#yourAge = int(raw_input("How old are you: "))
yourAge = 22
if(yourAge>0) and (yourAge < 110):
    if (yourAge == 21):
        print "Same as me"
    elif (yourAge > 21):
        print "Older than me"
    else:
        print "Youngerfrom me"
else:
    print "Don't lie about your age"

x, y=1, 0
a= 'y is less than x' if(y<x) else 'x is less than y'
print a
print "\n"

#tutorial 5
listEx5 = [1,2,3,4,5,6,7]
print 3 in listEx5
print 10 in listEx5

count = 1
while count <=10:
    print count,
    count+=1

print "\n"

for i in listEx5:
    print i,
for i in range(1,20):
    if (i%2!=0):
        continue
    elif i==16:
        break
    else:
        print i,
print "\n"

#tutorial 6
def addNumbers(*args):
    counter = 0
    if args:
        for i in args:
            counter+=i
        return counter
    else:
        print "provide numbers"

def factorial(num):
    if num == 1 :
        return 1
    else: return num * factorial(num-1)

'''def main():
    print addNumbers(10,20,30,40)
    print factorial(5)
if __name__== '__main__':main()'''
print "\n"

#tutorial 7,8,9,10
__metaclass__ = type

class Animal:
    __name = "No name"
    __owner = "No owner"
    def __init__(self,**kvargs):
        self._attributes = kvargs

    def set_attributes(self, key, value):
        self._attributes[key] = value
        return
    def get_attributes(self, key):
        print self._attributes.get(key)

    def noise(self):
        print ('errr')

    def move(self):
        print('the animal moves forward')
        return
    def eat(self):
        print('Crunch, Crunch')

class Dog(Animal):
    def __init__(self, **kvargs):
        super(Dog,self).__init__()
        self._attributes = kvargs

    def noise(self):
        print('Ham, Ham')
        Animal.noise(self)
        return

class Cat(Animal):
    def __init__(self, **kvargs):
        super(Cat,self).__init__()
        self._attributes = kvargs

    def noise(self):
        print('Meow, Meow')
        return

    def noise2(self):
        print('purrrr')
        return

def playwihtAninal(Animal):
    Animal.noise()
    Animal.eat()
    Animal.move()
    print(Animal.get_attributes('__name'))
    print(Animal.get_attributes('__owner'))
    print '\n'

def retriveFile():
    try:
        bestStudent ={}
        bestStudentStr = "The best student\n\n"

        f =open('studentgrades.txt')
    except(IOError), e:
        print "File not found", e
    else:
        for line in f:
            name1, grade = line.split()
            bestStudent[grade]=name1
        f.close()

        for i in sorted(bestStudent.keys(), reverse=True):
            print (bestStudent[i] + ' scored a ' + i)
            bestStudentStr += bestStudent[i] + ' scored a ' + i + '\n'
        print '\n'

        print bestStudentStr

        outToFile = open("studentrank.txt", "w")
        outToFile.write(bestStudentStr)
        outToFile.close()

        print "finished output"
    return

def main():
    mike = Dog(__name = 'Mike', __owner = 'Vlad')
    bela = Cat(__name='Bela', __owner='Tori')
    playwihtAninal(mike)
    playwihtAninal(bela)

    retriveFile()




if __name__ == '__main__': main()
print "\n"


