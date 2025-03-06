/**
 * @file AddressBook.cpp
 * @brief Implementation of the AddressBook class.
 *
 * This file contains the implementation of the methods defined in
 * the `AddressBook` class.
 */

#include "AddressBook.hpp"
#include <algorithm>
#include <string>

/**
 * @brief Adds a contact to the address book.
 *
 * @param contact A shared pointer to the contact to be added.
 */
void AddressBook::addContact(std::shared_ptr<Contact> contact)
{
    contacts.push_back(contact);
    std::cout << "Contact added successfully !" << std::endl;
}
/**
 * @brief Deletes a contact from the address book by name.
 *
 * @param name The name of contact to be deleted.
 */
void AddressBook::deleteContact(const std::string& name)
{
    auto it = std::find_if(contacts.begin(), contacts.end(), [&name](const std::shared_ptr<Contact>& contact){
        return contact->getName() == name;
    });
    if(it != contacts.end())
    {
        contacts.erase(it);
        std::cout << "Contact deleted successfully!" << std::endl;
    }
    else
    {
        std::cout << "Contact not found!" << std::endl;
    }
}
/**
 * @brief Deletes all contacts from the address book.
 */
void AddressBook::deleteAllContacts()
{
    if(contacts.empty())
    {
        std::cout << "Address book is already empty!" << std::endl;
    }
    else
    {
        contacts.clear();
        std::cout << "All contacts deleted successfully!" << std::endl;
    }
}
/**
 * @brief Searches for a contact by name and display its details.
 *
 * @param name The name of the contact to search for.
 */
void AddressBook::searchContact(const std::string& name) const
{
    auto it = std::find_if(contacts.begin(), contacts.end(), [&name](const std::shared_ptr<Contact>& contact){
        return contact->getName() == name;
    });

    if(it != contacts.end())
    {
        (*it)->display();
    }
    else
    {
        std::cout << "Contact not found!" << std::endl;
    }
}
/**
 * @brief Lists all contacts in the address book.
 */
void AddressBook::listContacts() const
{
    if (contacts.empty()) 
    {
        std::cout << "No contacts available in the address book." << std::endl;
    }
    else
    {
        std::cout << "Contacts in the address book:" << std::endl;
        for (const auto& contact : contacts) 
        {
            contact->display();
        }
    }
}