/**
 * @file main.cpp
 * @brief Main program for the Address Book application.
 *
 * This file implements the main logic of the address book application,
 * allowing users to interact with the address book through a menu-driven interface.
 */
#include "AddressBook.hpp"
#include "PersonalContact.hpp"
#include "BusinessContact.hpp"
#include <iostream>
#include <memory>
#include <string>

int main()
{
    /**
     * @var addressBook
     * An instance of the AddressBook class to manage contacts.
     */
    AddressBook addressBook;
    std::string command;

    std::cout << "Welcome to your favourite address book!" << std::endl;

    while(true)
    {
        // Menu options
        std::cout << "\nWhat do you want to do?" << std::endl;
        std::cout << "| List       | Lists all users" << std::endl;
        std::cout << "| Add        | Adds a user" << std::endl;
        std::cout << "| Delete     | Deletes a user" << std::endl;
        std::cout << "| Delete all | Removes all users" << std::endl;
        std::cout << "| Search     | Searches for a user" << std::endl;
        std::cout << "| Close      | Closes the address book" << std::endl;
        std::cout << "> ";
        std::cin >> command;

        if(command == "List")
        {
            addressBook.listContacts();
        }
        else if(command == "Add")
        {
            std::string type;
            std::cout << "Enter contact type (Personal/Business): " << std::endl;
            std::cin >> type;

            if(type == "Personal")
            {
                std::string name, phoneNumber, relationship;
                std::cout << "Enter the name: " << std::endl;
                std::cin.ignore(); // Clear the input buffer
                std::getline(std::cin,name);
                std::cout << "Enter the phone number: " << std::endl;
                std::getline(std::cin,phoneNumber);
                std::cout << "Enter the relationship: " << std::endl;
                std::getline(std::cin,relationship);
                addressBook.addContact(std::make_shared<PersonalContact>(name,phoneNumber,relationship));
            }
            else if(type == "Business")
            {
                std::string name, phoneNumber, company;
                std::cout << "Enter the name: " << std::endl;
                std::cin.ignore(); // Clear the input buffer
                std::getline(std::cin,name);
                std::cout << "Enter the phone number: " << std::endl;
                std::getline(std::cin,phoneNumber);
                std::cout << "Enter the company: " << std::endl;
                std::getline(std::cin,company);
                addressBook.addContact(std::make_shared<BusinessContact>(name,phoneNumber,company));
            }
            else
            {
                std::cout << "Invalid contact type!" << std::endl;
            }
        }
        else if(command == "Delete")
        {
            std::string name;
            std::cout << "Enter the name of the contact to  delete: " << std::endl;
            std::cin.ignore(); // Clear the input buffer
            std::getline(std::cin,name);
            addressBook.deleteContact(name);
        }
        else if(command == "Delete all")
        {
            addressBook.deleteAllContacts();
        }
        else if(command == "Search")
        {
            std::string name;
            std::cout << "Enter the name of contact to search: " << std::endl;
            std::cin.ignore(); // Clear the input buffer 
            std::getline(std::cin,name);
            addressBook.searchContact(name);
        }
        else if(command == "Close")
        {
            std::cout << "Closing the address book. Goodbye!" << std::endl;
            break;
        }
        else
        {
            std::cout << "Invalid command! Please try again." << std::endl;
        }
    }
    return 0;
}