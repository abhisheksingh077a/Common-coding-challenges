# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:17:35 2019

@author: Abhishek singh
"""
def findPalindrome(number):
    temp_number  = number
    digits_of_num = []
    
    while(temp_number > 0):
        digits_of_num.append(temp_number % 10)
        temp_number = int(temp_number / 10)
        
    digits_of_num.reverse()
    
    for ii in range(len(digits_of_num)):
        temp_number += digits_of_num[ii] * pow(10, ii)
        
    print("reversed number is: ", temp_number)
    return (temp_number == number);    

"""
    A given number is palinedrome if:
        
    the number made from reversing the digit is equal to the original number
"""

if __name__ == "__main__":
        
    number = int(input("Enter a number to check if number is palindrome or not: "))
    if(findPalindrome(number) == 1):
        print("number ", number, " is palindrome")
    else:
        print("number", number, " is not palindrome")
    