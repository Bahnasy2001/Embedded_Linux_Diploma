#include <iostream>

int main()
{
    int a,b,c;
    std::cout<<"Enter first Number:";
    std::cin>>a;
    std::cout<<"Enter Second Number:";
    std::cin>>b;
    std::cout<<"Enter Third Number:";
    std::cin>>c;
    std::cout<<"========================"<<std::endl;
    if (a > b) 
    {
        if(a > c)
        {
            std::cout<<"The Maximum Number is "<<a<<std::endl;
        }
        else
        {
            std::cout<<"The Maximum Number is "<<c<<std::endl;
        }    
    }
    else
    {
        if(b > c)
        {
            std::cout<<"The Maximum Number is "<<b<<std::endl;
        }
        else
        {
            std::cout<<"The Maximum Number is "<<c<<std::endl;
        }
    }
    return 0;
}