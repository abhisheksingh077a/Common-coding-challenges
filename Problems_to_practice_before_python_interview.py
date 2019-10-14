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

