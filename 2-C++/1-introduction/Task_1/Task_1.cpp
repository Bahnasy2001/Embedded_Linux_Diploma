#include <iostream>

int main()
{
    std::cout<<"ASCII Code Table:"<<std::endl;
    std::cout<<"+------+-------+"<<std::endl;
    std::cout<<"| Char | ASCII |"<<std::endl;
    std::cout<<"+------+-------+"<<std::endl;
    for (int i = 0; i < 128; i++)
    {
        std::cout<<"|    "<<char(i)<<" |"<<"     "<<i<<"  |"<<std::endl;
    }
    return 0;
}