
class Counter: 
    def __init__(self, start: int=0) -> None: 
        self.value = start

    def increment(self) -> None: 
        self.value += 1

    def current_value(self) -> int: 
        return self.value


c=Counter(start=5) #creating an object from the Counter class


c1=Counter(start=10) #creating an object from the Counter class

c1.increment() #calling the increment method on the object c1

print(f"c1: {c1.current_value()}") #calling the current_value method on the object c1 and printing the result
print(f"c1: {c1.current_value()}")