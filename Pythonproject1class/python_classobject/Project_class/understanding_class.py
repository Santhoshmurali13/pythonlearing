# import class from another python file
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))


from python_classobject.calculation import Do_calculation


class school:
    
    name = "Santhosh"
    
    def address(self):
        print("Rajajinagar, Bangalore")
        # to call variable from another methof
        print(self.name)

    def gender(self):
        print("male")    
# to call one method from another method
        self.address()

# Create and object of the class
obj = school()
obj.address()
obj.gender
print(obj.name)

obj1 = Do_calculation()
obj1.Addition(5,6)
