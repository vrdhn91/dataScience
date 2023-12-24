// Exercise1_Task2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>

int main()
{
    /*Floating point types :
    1. Adapt the code from the "Simple I/O" page
        2. For a single user - given double, have your program print the number rounded down,
        rounded up and it's square root;
        what is the behaviour for negative numbers ?
        3. Find out how to change the precision of the output stream so more / less digits are
        printed.
        4. Find out how to change the output format to always show 1e-02 instead of 0.01.*/
    std::string s{ "foo" };
    std::cout << "Welcome to the " << s << " program!\n";
    std::cout << "Enter two floating point numbers followed by [RETURN]\n";
    double d1{};
    double d2{};
    std::cin >> d1 >> d2;
    std::cout << "The sum is: " << d1 + d2 << '\n';
    std::cout << "Round up: " << std::ceil(d1 + d2) << '\n';
    std::cout << "Round down: " << std::floor(d1 + d2) << '\n';
    std::cout << "Square root: " << std::sqrt(d1 + d2) << '\n';
    /*Round up for negative value will round the value up closer to 0.
    Round down for negative value will round the value down further from 0.
    Square root will return nan*/
    std::cout << "Set precision to 3 floating points: " 
        << std::setprecision(3) << std::fixed << std::sqrt(d1 + d2) << '\n';
    std::cout << "Change decimal format to scientific notation: "
        << std::scientific << std::sqrt(d1 + d2) << '\n';
}