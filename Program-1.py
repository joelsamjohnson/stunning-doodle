class Calculator:

    def add(self,num1, num2):
        return num1+num2;

    def sub(self,num1,num2):
        return num1-num2

    def mul(self, num1, num2):
        return num1*num2;

    def div(self,num1,num2):
        return num1/num2;


obj=Calculator()
a=int(input("enter a number"))
b=int(input("enter another number"))
op=input("enter operation")

if op == "+":
    res = obj.add(a,b)

elif op == "-":
    res = obj.sub(a,b)

elif op == "*":
    res = obj.mul(a,b)

elif op == "/":
    res = obj.div(a,b)

print(res)

