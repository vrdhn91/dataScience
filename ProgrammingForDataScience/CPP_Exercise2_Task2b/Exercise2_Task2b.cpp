#include <iostream>

template <typename T>
void print(T const i)
{
	std::cout << "Integer!\n";
}
void print(float const i)
{
	std::cout << "Floating point!\n";
}
int main()
{
	float a{3.3}; //initialize the variable
	print(a);
}