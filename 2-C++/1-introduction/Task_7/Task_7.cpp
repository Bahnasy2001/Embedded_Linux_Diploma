#include <iostream>
#include <bitset>
int main()
{
    int dec;
    std::string binaryString;
    // Decimal To Binary
    std::cout<<"Enter a decimal Number: ";
    std::cin>>dec;
    std::bitset<8>binary(dec);
    std::cout<<"Binary representation: "<<binary.to_string()<<std::endl;
    // Binary To Decimal
    std::cout<<"Enter a binary Number: ";
    std::cin>>binaryString;
    std::bitset<8>bin(binaryString);
    std::cout<<"Decimal representation: "<<bin.to_ullong();
    return 0;
}