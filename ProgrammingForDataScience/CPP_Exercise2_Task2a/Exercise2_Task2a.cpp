// Exercise2_Task2a.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

double square(double const d); // declaration
double square1(double e); // declaration
double& square2();
int& test();

/*What happens when you return something of const type from a function ? Can
constants be initialised from functions that return a non - const type ?*/

int main()
{
    std::cout << "Enter number: ";
    double e{};
    std::cin >> e;
    // ↓ must be declared before
    //What happens when you return something of const type from a function ?
    /*It is possible.but the value will be constance, meaning it can not be changed*/
    std::cout << "The square is : " << square(e) << '\n';

    //Can constants be initialised from functions that return a non-const type?
    /*Constants can be initialized inside a function and it can be return as a non - constants
    function. In this case double*/
    double g = square1(e);
    g = 8.1;
    std::cout << "The square is 1: " << g << '\n';
    
    //What happens when you return a reference? What about the example on slide 20?
    /*The program still runs, but i think it returns the memory location during the runtime*/
    double & f = square2();
    std::cout << "Return reference: " << f << '\n';
    
    //What combinations of const, const &, & (and none) are there for variables and for
    //function return values ? Which combinations are valid / invalid for initialising the
    //variable ?
    /*const is valid for both variable and return value
    const &  is valid for both variable and return value
    & is valid but it doesn't return the value as expected because may be the lifetime 
    of the variable is only inside that function*/

    int& z = test();
    std::cout << "Reference z: " << z << '\n';

}

int & test() {
    int b = 5;
    std::cout << "b: " << b << '\n';
    int & a = b;
    b = 6;
    std::cout << "a: " << a << '\n';
    return a;
}

double square(double const d) // definition
{
    return d;
}

double square1(double e) // definition
{
    const int a = 7;
    return a;
}

double & square2()
{
    double d{ 7.9 };
    return d;
}
