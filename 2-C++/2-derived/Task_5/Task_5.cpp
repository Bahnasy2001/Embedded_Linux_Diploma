// Task 5: find the even and odd numbers in the array

#include <iostream>
#include <vector>

// Function to separate even and odd numbers from array
void findEvenAndOdd(const std::vector<int>& arr, std::vector<int>& evens, std::vector<int>& odds)
{
    // Iterate through the array and classify each number as even or odd
    for (const int& num : arr) 
    {
        if(num % 2 == 0)
        {
            evens.push_back(num); // Add to the evens vector if the number is even
        }
        else 
        {
            odds.push_back(num); // Add to the odds vector if the number is odd
        }
    }
}

int main()
{
    // Example array
    std::vector<int> numbers = {1,2,3,4,5,6,7,8,9,10};

    // Vectors to store even and odd numbers
    std::vector<int> evenNumbers;
    std::vector<int> oddNumbers;

    // Call the function to separate even and odd numbers
    findEvenAndOdd(numbers, evenNumbers, oddNumbers);

    // Display Even Numbers
    std::cout << "Even Numbers: ";
    for (const int& num : evenNumbers) 
    {
        std::cout << num<< " ";
    }
    std::cout << std::endl;

    // Display Odd Numbers
    std::cout << "Odd Numbers: ";
    for (const int& num : oddNumbers) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}