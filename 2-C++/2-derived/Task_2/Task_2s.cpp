/* Task 2: create a function to 
* search to the number in the array which number is taken from user
*/
#include <iostream>
#include <vector>

// Function to search for a number in the array
int searchNumber(const std::vector<int>& arr, int target)
{
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] == target)
        {
            return i; // Return the index where the number is found
        }
    }
    return -1; // Return -1 if the number is not found
}

int main()
{
    // Example array
    std::vector<int> numbers = {3,5,7,2,-1,8,4,10,12};
    
    // Prompt the user to enter a number to search for
    int target;
    std::cout << "Enter the number you want to search for: ";
    std::cin >> target;

    // Call the search Function
    int result = searchNumber(numbers,target);

    // Output the result
    if (result != -1)
    {
        std::cout << "The number " << target << " is found at index " << result << "." << std::endl;
    }
    else
    {
        std::cout << "The number " << target << " is not found in the array." << std::endl;
    }
    return 0;
}