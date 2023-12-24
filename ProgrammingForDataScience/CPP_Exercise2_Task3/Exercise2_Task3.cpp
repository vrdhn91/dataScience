// Exercise2_Task3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int fibonacci(int a, int b, int c);

int main()
{
    int n1{};
    int n2{};
    int c{};
    std::cin >> n1 >> n2 >> c;
    int z = fibonacci(n1, n2, c);
    std::cout << "The " << c << "-th Fibonacci Number : " << z;

}

int fibonacci(int n1, int n2, int c) {
    int temp{};
    int& result = temp;
    if (c>2) {
        temp = n1 + n2;
        std::cout << "temp: " << temp <<"\n";
        result = fibonacci(n2, temp, c - 1);
    }
    else {
        //std::cout << "Fibonacci Number: " << n2 << "\n";
        return n2;
    }
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
