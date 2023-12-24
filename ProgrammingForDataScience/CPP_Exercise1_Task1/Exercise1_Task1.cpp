// Exercise1_Task1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <limits>

int main()
{
    //std::cout << "Hello World!\n";

    /*1. Write a program that prints for the types char, short, int, long, long long and the
        respective unsigned versions :
            1. the size in bits
            2. the largest possible value(find the C++ way, not the C way)
            3. the smallest possible value(find the C++ way, not the C way)
     2. What happens when you assign a value that is too large / small ? Is this defined
        behaviour(according to the C++ standard) ?*/
    std::cout << "Size in bits: \n";
    std::cout << "char: " << sizeof(char) * CHAR_BIT << " bit\n";
    std::cout << "short: " << sizeof(short) * CHAR_BIT << " bit\n";
    std::cout << "int: " << sizeof(int) * CHAR_BIT << " bit\n";
    std::cout << "long: " << sizeof(long) * CHAR_BIT << " bit\n";
    std::cout << "long long: " << sizeof(long long) * CHAR_BIT << " bit\n";

    std::cout << "\n\nLargest possible value: ";
    std::cout << "\nchar: " << std::numeric_limits<char>::max();
    std::cout << "\nshort: " << std::numeric_limits<short>::max();
    std::cout << "\nint: " << std::numeric_limits<int>::max();
    std::cout << "\nlong: " << std::numeric_limits<long>::max();
    std::cout << "\nlong long: " << std::numeric_limits<long long>::max();

    std::cout << "\n\nSmallest possible value: ";
    std::cout << "\nchar: " << std::numeric_limits<char>::min();
    std::cout << "\nshort: " << std::numeric_limits<short>::min();
    std::cout << "\nint: " << std::numeric_limits<int>::min();
    std::cout << "\nlong: " << std::numeric_limits<long>::min();
    std::cout << "\nlong long: " << std::numeric_limits<long long>::min();

    //Assigned value that is too large
    //int x_large = 2147483650;
    std::cout << "\nmax int: " << std::numeric_limits<int>::max();
    std::cout << "\nvalue assigned to int: 2147483650";
    //std::cout << "\nvalue int: " << x_large;
    //Assigning a value that is too big will result error
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
