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
