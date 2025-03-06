/* Task 2: create a function to 
* search to the number in the array which number is taken from user
*/
#include <iostream>
#include <vector>
int isFound(std::vector<int> numbers, int num)
{
    for (int i = 0; i < numbers.size(); i++)
    {
        if(num == numbers[i]) return i;
    }
    return -1;
}

#include <iostream>
int main()
{
    std::vector<int> numbers = {3,5,7,2,-1,8,4,10,12};
    int num;
    std::cout << "Enter The Number: ";
    std::cin >> num;
    int result = isFound(numbers,num);
    if (result != -1) 
    {
    std::cout << "Num " << num << " is found in index " << result << std::endl;
    }
    else
    {
        std::cout << "Num " << num << " is not found" << std::endl;
    }
    return 0;
}