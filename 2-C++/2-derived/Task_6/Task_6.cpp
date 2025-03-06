/*
Simple Lambda: Write a lambda function to calculate the square of a given number.
Sort with Lambda: Use lambda functions to sort an array of integers in ascending and descending
order.
 */

#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    // Define a lambda function to calculate the square of a number
    auto square = [](int x) -> int {return x*x;};

    // Test the lambda function
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;

    std::cout << "Square of " << num << " is " << square(num) << std::endl;

    // Example array
    std::vector<int> numbers = {5, 3, 8, 1, 9, 2, 7};
    // Display original array
    std::cout << "Original array: ";
    for (const int& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Sort in ascending order using a lambda function
    std::sort(numbers.begin(),numbers.end(),[](int a, int b){ return a > b;});
    
    // Display sorted array in ascending order
    std::cout << "Array sorted in ascending order: ";
    for (const int& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Sort in descending order using a lambda function
    std::sort(numbers.begin(),numbers.end(),[](int a, int b) {return a < b;});

    // Display sorted array in descending order
    std::cout << "Array sorted in descending order: ";
    for (const int& num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}