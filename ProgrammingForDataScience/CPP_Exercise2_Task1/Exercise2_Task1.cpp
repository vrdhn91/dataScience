// Exercise2_Task1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int main()
{
    std::cout << "Hello World!\n";
	std::string name{};
	std::int64_t postcode{};
	char input{};

    do {
		std::cout << "Input name : \n";
		std::cin >> name;
		std::cout << "Input postcode: \n";
		std::cin >> postcode;

		if (postcode >= 10115 and postcode <= 14199) {
			std::cout << name << " lives in Berlin \n";
		}
		else
		{
			std::cout << name << " lives outside of Berlin \n";
		}

		std::cout << "Enter another person? [y/n] : \n";
		std::cin >> input;
		
	}while (input == 'y');
}

