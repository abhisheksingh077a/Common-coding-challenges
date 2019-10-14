#Question: 1
# Input a digit and the output the sum  as following:
        #let digit is 9 output 9 + 99 + 999 + 9999
    
def rept(num):
    value = 0
    for ii in range(1, 5):
        value = value + int(str(num) * ii)
    return value

num = int(input("enter a number to find sum as a + aa + aaa + aaaa"))
print(rept(num))

#Question: 2
#Take input as comma-seaprated values from console 
#filer odd numbers
#output these as comma separated strings

#Sample:  Input:  1,2,3,4,5,6,7,8
         #Output:  1,3,5,7

        
st = input("Enter comma-separted values: ")

odd = []

st = st.split(",")
for value in st:
    if int(value) % 2:
        odd.append(value)

print("Input: ", ",".join(st))
print("Output: ", ",".join(odd))



# Question: 3
# find the total money in a bank account by using log book entries
# input D 500,W 300,D 200   D:deposit   W:withdrawl
# total money is a/c: 400

def bnk_balance(st):
    st = st.split(",")
    blnc = 0
    for item in st:
        item = item.split(" ")
        if(item[0] == "D"):
            blnc = blnc + int(item[1])
        elif(item[0] == "W"):
            blnc = blnc - int(item[1])
    return blnc

if __name__ == "__main__":
    st = input("Enter the log book in given format: ")
    print(bnk_balance(st))

      
#Question: 4
# using a generator ouput fibonacci series upto a given number
# input : 10
# ouput : 1,1,2,3,5,8

def fibo(limit):
    a = 0
    b = 1
    while(b <= limit):
        yield b
        a, b = b, a + b
        
num = int(input("Enter an intger to generate the fibonacci series upto the number: "))
fib = []
for value in fibo(num):
    fib.append(str(value))
    
print(",".join(fib))


#Question 5
# input : a string which are comma separeted passwords to an account
# output : list of comma-separated valid passwords
# criteria :
#1: atleast 1 lower_case(a-z)
#2: atleast one number(1-9)
#3: atleast one upper case(A-Z)
#4: atleast one [$,#,@]
#5: length should be between(6, 12)
#input Abh@i123,abhi234,apple@3&78
#ouput Abh@i123
def valid(st):
    st = st.split(",")
    pass_list = []
    for item in st:
        digit = 0
        lower = 0
        upper = 0
        splstr = 0
        if(len(item) > 5 and len(item) < 13):
            for ii in range(len(item)):
                if str.isdigit(item[ii]):
                    digit += 1
                elif str.isalpha(item[ii]):
                    if(str.islower(item[ii])):
                        lower += 1
                    elif(str.isupper(item[ii])):
                        upper += 1
                    else:
                        pass
                elif item[ii] == "@" or item[ii] == "#" or item[ii] == "$":
                    splstr += 1
                else:
                    pass
        else:
            continue
        
        if(digit > 0 and lower > 0 and upper > 0 and splstr > 0):
            pass_list.append(item)
        else:
            pass
    return pass_list
import re
def valid_using_re(st):
    st = st.split(",")
    pass_list = []
    for item in st:
        if len(item) < 6 or len(item) > 12:
            continue
        
        elif re.search("[a-z]", item) != None and re.search("[A-Z]", item) != None and re.search("[@#$]", item) != None and re.search("[0-9]", item) != None:
            pass_list.append(item)
        else:
            pass
    return pass_list

st = input("enter the passwords as comma-separated values")

st2 = valid_using_re(st)
st1 = valid(st)
print(",".join(st2))
print(",".join(st1))
