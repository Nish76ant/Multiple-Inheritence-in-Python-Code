class Employee:

    noOfLeaves = 8
    var = 8

    def __init__(self,name,role,salary):
           self.name = name
           self.role = role
           self.salary = salary

    def printDetailsofEmp(self):
        return f'Hey your name is {self.name} and your role  is {self.role} and your salary is {self.salary}'

    @classmethod
    def changeOfleaves(cls,newleaves):
           cls.noOfLeaves = newleaves 

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        #print(params)
        return cls(params[0],params[1],params[2])
    
    @staticmethod
    def printgood(string):
        print('This is good'+string)  
        return 'Hii' 


class Player:
    noOfGames = 4
    var = 9

    def __init__(self,name,game):
        self.name = name 
        self.game = game

    def printdetails(self):
        return f' the name is {self.name} and game is {self.game}'

class coolprogrammer(Employee,Player):
    language = "C++"
    var = 10

    def printlange(self):
        return f'{self.language}'



Rajan = Employee('Rajan','Developer',25000)
rohan = Employee('Rohan','Computer Science Engineer',25000)
shubham = Player('Shubham',['Cricket'])
karan = coolprogrammer('Karan',34000,'Cool Programmer')
print(karan.printlange())
print(karan.var)
#det = karan.printDetailsofEmp()
#print(karan.language)
#print(karan.noOfGames)
#print(det)
