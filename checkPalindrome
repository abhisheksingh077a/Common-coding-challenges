#include <iostream>
#include <vector>
#include <cmath>
int palindrome(int number)
{
std::vector<int> digits_of_number;
int temp_number{number};
    while(temp_number > 0)
    {
        digits_of_number.push_back(temp_number % 10);
        //std::cout << (temp_number % 10) << "\n";
        temp_number = static_cast<int>(temp_number / 10);
    }

    temp_number = 0;
    int length = digits_of_number.size();
    for(int ii = 0; ii < length; ii ++)
    {
        //std::cout << digits_of_number[ii];
        temp_number += digits_of_number[ii] * std::pow(10, length - 1 - ii);
    }
    
    std::cout << "\n Reversed number is " << temp_number << "\n";
    if(temp_number == number)
        return 1;
    else
        return 0;
}

int main()
{
    std::cout << "\n Enter a number to check if it is palindrome or not: ";
    int number = 0;
    std::cin >> number;
    if(palindrome(number) == 1)
        std::cout << "\n Hence " << number << " is palindrome ! \n";
    else
        std::cout << "\n Hence " << number << " is not palindrome ! \n";
return 0;
}
