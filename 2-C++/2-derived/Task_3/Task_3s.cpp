// Task 3: delete number in array

#include <iostream>
#include <vector>


bool deleteNumber(std::vector<int>& arr,int target)
{
    for (auto it = arr.begin(); it != arr.end(); it++) 
    {
        if (*it == target)
        {
            arr.erase(it); // Erase the element at the iterator position
            return true; // Return true to indicate successful deletion
        }
    }
    return false; // Return false if the number was not found
}

void deleteAllOccurrences(std::vector<int>& arr, int target) {
    auto it = arr.begin();
    while (it != arr.end()) {
        if (*it == target) {
            it = arr.erase(it); // Erase the element and update the iterator
        } else {
            ++it; // Move to the next element
        }
    }
}
int main()
{
    // Example vector
    std::vector<int> numbers = {3, 5, 7, 2, 8, -1, 4, 10, 12,4};
    
    // Prompt the user to enter a number to delete
    int target;
    std::cout << "Enter the number you want to delete: ";
    std::cin >> target;

    // Call the delete function
    if (deleteNumber(numbers, target))
    {
        deleteAllOccurrences(numbers, target);
        std::cout << "The number " << target << " has been successfully deleted." << std::endl;
    }
    else
    {
        std::cout << "The number " << target << " was not found in the array." << std::endl;
    }

    // Display the updated array
    std::cout << "Update array: ";
    for (const int& num : numbers) 
    {
        std::cout << num << " " ;
    }
    std::cout << std::endl;
    return 0;
}