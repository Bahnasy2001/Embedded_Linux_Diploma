// Task 1: create a function to find the maximum number of array
#include <exception>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>

template <typename T>
T findMaximum (const std::vector<T>& arr)
{
    if(arr.empty())
    {
        throw std::invalid_argument("Array is empty. Cannot determine the maximum.");
    }

    T maxVal = std::numeric_limits<T>::lowest(); // Initialize to the lowest possible value
    for (const T& num : arr) 
    {
        if (num > maxVal) 
        {
            maxVal = num; // Update maxVal if current number is greater
        }
    }
    return maxVal;
}

int main()
{
    try {
    // Example usage:
        std::vector<int> numbers = {3,5,7,2,-1,8,4,10,12};
        int maxNumber = findMaximum(numbers);
        std::cout << "The Maximum number in the array is " << maxNumber << std::endl;

        // Example with floating-point numbers:
        std::vector<double> floatNumbers = {3.5, 5.2, 7.8, 2.1, 8.9, -1.3, 4.6, 10.1, 12.7};
        double maxFloat = findMaximum(floatNumbers);
        std::cout << "The Maximum number in the float array is " << maxFloat << std::endl;
    } catch (const std::exception& e) 
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    return 0;
}