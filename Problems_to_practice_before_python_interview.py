# Input a digit and the output the sum  as following:
        #let digit is 9 output 9 + 99 + 999 + 9999
    
def rept(num):
    value = 0
    for ii in range(1, 5):
        value = value + int(str(num) * ii)
    return value

num = int(input("enter a number to find sum as a + aa + aaa + aaaa"))
print(rept(num))

