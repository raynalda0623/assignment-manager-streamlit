
class Counter: 
    def __init__(self, start: int=0, step: int=1) -> None: 
        self.value = start

    def increment(self) -> None: 
        self.value += 1

    def current_value(self) -> int: 
        return self.value
    
    def increment_2(self):
        self.value += 2

c=Counter(start=5) #creating an object from the Counter class


c1=Counter(start=10) #creating an object from the Counter class

c1.increment() #calling the increment method on the object c1

print(f"c1: {c1.current_value()}") #calling the current_value method on the object c1 and printing the result
print(f"c1: {c1.current_value()}")

c.increment_2() #calling the increment_2 method on the object c
print(f"c: {c.current_value()}") #calling the current_value method on the object c and printing the 


# Session 2 out of 00 - Employee Example
class Employee:
    def _init_(self, name, base_salary: float)-> None:
        self.name = name
        self.base_salary = base_salary

    def calc_bonus(self, bonus_percentage: float) -> float:
        return self.base_salary * bonus_percentage

emp= Employee("Alice", 50000.0) #initiate an object from the class/ create an object from the class

bonus = emp.calc_bonus(0.1) #call the method calc_bonus on the object emp and store the result in the variable bonus
print(f"Bonus for {emp.name} is {bonus}") #print the bonus for the employee