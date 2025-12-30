Python does not support traditional method overloading.
The last method definition wins.

class Poly:
    def m1(self,a):
        print("Value of the variable : ",a)
        
    def m1(self,a,b):
        result = a+b
        print("Result : ",result)
        return result

p1 = Poly()
p1.m1(1)
p1.m1(1,4)

p1.m1(1) --> fails -> TypeError: m1() missing 1 required positional argument: 'b'

