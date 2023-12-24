// Exercise3_Task1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

template <typename TLambda>
std::vector<size_t> filter(std::vector<size_t> const& input, TLambda const& l) {
    std::vector<size_t> newVector;
    for (size_t a : input) {
        if (l(a)) {
            newVector.push_back(a);
        }
    }
    return newVector;
}

int main()
{
    auto even = [](size_t elem) { return elem % 2 == 0; };
    auto odd = [](size_t elem) { return elem % 2 != 0; };
    auto notZero = [](size_t elem) { return elem != 0; };
    std::vector<size_t> ds{ 0, 2, 3, 5, 6, 8};
    std::vector<size_t> even_vec = filter(ds, even);
    std::vector<size_t> odd_vec = filter(ds, odd);
    std::vector<size_t> notZero_vec = filter(ds, notZero);
    for (size_t b:even_vec) {
        std::cout << "\nEven: " << b;
    }
    for (size_t b : odd_vec) {
        std::cout << "\nOdd: " << b;
    }
    for (size_t b : notZero_vec) {
        std::cout << "\nNot Zero: " << b;
    }
    
}

