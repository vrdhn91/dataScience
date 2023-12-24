// Exercise1_Task3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

int main()
{
    
    /*Out-of-bounds:
    1. Write a program that reads a string from the user input and then a number
    2. print the i-th character of the string to the user (where i is the number supplied by
    the user)
    3. What happens when the number is larger than the string is big?
    4. Did you use operator[] or .at() to access the string? Try both and compare the
    behaviour!*/

    std::string inputString = "";
    int inputNumber{};
    std::cout << "Input String : \n";
    std::cin >> inputString;
    std::cout << "Input number: \n";
    std::cin >> inputNumber;
    std::cout << "The : " << inputNumber << " - th character is : " << inputString[inputNumber]<< "\n";
    /*If number is bigger than the string length, then runtime error: string subscript out of range*/
    std::cout << "Access string using .at() : " << inputString.at(inputNumber) << "\n";
    /*The result is the same between accessing index using[] or .at().The difference when
    I input number bigger than the string length. .at() throws different error message during runtime*/
}