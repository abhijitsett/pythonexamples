class Poly:
    def m1(self, *args):
        if len(args) == 1:
            print("Value :", args[0])
        elif len(args) == 2:
            print("Result :", args[0] + args[1])
    
    def m2(self,*args):
        for p in args:
            print(p)

p1 = Poly()
p1.m1(1)
p1.m1(1,4)

p1.m2(10)
p1.m2(10,20)