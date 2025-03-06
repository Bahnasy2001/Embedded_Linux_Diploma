// Task 4: merge two arrays together

#include <iostream>
#include <vector>
#include <algorithm>

// Function to merge and sort two vectors
std::vector<int> mergeAndSortArrays(const std::vector<int> arr1,const std::vector<int> arr2)
{
    // Create a new vector to store the merged result
    std::vector<int> mergedArray;

    // Add all elements from first array
    for (const int& num : arr1) 
    {
        mergedArray.push_back(num);
    }
    
    // Add all elements from second array
    for (const int& num : arr2) 
    {
        mergedArray.push_back(num);
    }

    // Sort the merged Array
    std::sort(mergedArray.begin(),mergedArray.end());

    return mergedArray;
}

int main()
{
    // Example
    std::vector<int> numbersOne = {3, 5, 7, 2, 8, -1, 4, 10, 12};
    std::vector<int> numbersTwo = {1,6,13,-3,0,18};

    // Merge and sort the two arrays
    std::vector<int> mergedArray = mergeAndSortArrays(numbersOne, numbersTwo);

    // Display the merged and sorted array
    std::cout << "Merged and Sorted array: ";
    for (const int& num : mergedArray) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}