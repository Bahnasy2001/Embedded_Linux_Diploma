#include <iostream>

int main()
{
    char x;
    std::cin>>x;
    switch (x) 
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            std::cout<<"The letter is vowel!"<<std::endl;
            break;
        default:
            std::cout<<"The letter is not vowel!"<<std::endl;
    }
    return 0;
}