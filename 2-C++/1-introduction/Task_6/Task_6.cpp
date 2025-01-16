#include <iostream>

int main()
{
    int num;
    int result = 0;
    int digit =0;
    std::cout<<"Enter Number: ";
    std::cin>>num;
    while(num % 10 != 0)
    {
        digit = num % 10;
        result += digit;
        num /= 10;
    }
    std::cout<<"\nSumming of Digits equal "<<result<<std::endl;
    return 0;
}