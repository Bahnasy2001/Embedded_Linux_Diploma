// Task 1: create a function to find the maximum number of array
#include <iostream>
#include <vector>

int findMax(std::vector<int> numbers)
{
    int max = numbers[0];
    for (int i = 0; i < numbers.size(); i++) 
    {
        if(numbers[i] > max)
        {
            max = numbers[i];
        }    
    }
    return max;
}

int main()
{
    std::vector<int> numbers = {4,7,8,2,9,3};
    int result = findMax(numbers);
    std::cout << "Max = " << result << std::endl;
    return 0;
}