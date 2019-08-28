#include"stringReversal.h"
#include<iostream>
#include<string>

void reverseString ( ) {

    std :: string name { "" } ;
    std :: cout <<"\nEnter you name : " ;
    std :: getline ( std::cin, name ) ; // read a full line of text into name
    int stringLength { static_cast <int>( name . length () ) } ;
    std :: cout << "\nString length is : " << stringLength << std ::endl ;
    
    for ( int i = 0 ; i <  ( stringLength / 2 ) ; i ++ ) {

        char temp { name [ i ] } ;
        std :: cout << temp << " <-- " << name [ (stringLength-1) - i] << std :: endl ;
        name [ i ] = name [ (stringLength-1) - i ] ;
       
        name [ (stringLength-1) - i ] = temp ;
    }

    std :: cout << "\nReverse of your name is : " << name ;


}