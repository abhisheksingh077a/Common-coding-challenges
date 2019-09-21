#include <iostream>

enum Message
{
    FOUND = 0,
    NOT_FOUND = 1,
    MAX_LENGTH = 2,
};

int find(int value, int length, int (&rnum)[9])
{
    for(int ii = 0; ii < length; ii ++)
    {
        if(rnum[ii] == value)
        {
            std::cout << "\n Value " << value << " found at index " << ii;
            return FOUND;
        }
            
    }
std::cout << "\n Value " << value << " doesnt exist in the array !" ;
return NOT_FOUND;
}

int main()
{
    int num[] = {61, 32, 63,94, 58, 66, 88, 99, 193};

    int length = sizeof(num) / sizeof(num[0]);

    std::cout << "\n length: " << length << "\n";
    std::cout << "\n Array: [";
    for(int ii = 0; ii < length; ii ++)
        std::cout<<num[ii] << " ";
    std::cout << "]" << "\n";
    std::cout << "\n Enter the num to search in array:  ";
    int snum = 0;
    std::cin >> snum;
    find (snum, length, num);
    return 0;
}
