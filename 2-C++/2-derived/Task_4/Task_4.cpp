// Task 4: merge two arrays together

#include <iostream>
#include <vector>

void merge (std::vector<int>& arrOne,std::vector<int>& arrTwo)
{
    for (const int& num : arrTwo) 
    {
        arrOne.push_back(num);
    }
}

int main()
{
    // Example
    std::vector<int> numbersOne = {3, 5, 7, 2, 8, -1, 4, 10, 12};
    std::vector<int> numbersTwo = {1,6,13,-3,0,18};

    merge(numbersOne, numbersTwo);
    // Display the updated array
    std::cout << "Update array: ";
    for (const int& num : numbersOne) 
    {
        std::cout << num << " " ;
    }
    std::cout << std::endl;
    
}