print("iti")

def sumnum(num1, num2):
    print(num1 + num2)

myd = {'num1':10, 'num2':20}
sumnum(**myd) # sumnum(num1=10, num2=20)
