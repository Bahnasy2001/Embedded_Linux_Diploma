#include <iostream>
#include <ostream>

int main()
{
    int x;
    std::cout<<"Enter The Number To Display its Multiplication Table: ";
    std::cin>>x;
    std::cout<<"==============================================="<<std::endl;
    for (int i = 1; i < 13; i++)
    {
        std::cout<<x<<" * "<<i<<" = "<<x*i<<std::endl;
    }
    return 0;
}