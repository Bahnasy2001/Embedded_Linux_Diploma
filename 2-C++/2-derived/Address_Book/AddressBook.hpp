/**
 * @file AddressBook.hpp
 * @brief Manages a collection of contacts in the address book.
 *
 * This file defines the `AddressBook` class, which manages a vector of contacts
 * and provides methods for adding, deleting, searching, and listing contacts.
 */

#ifndef ADDRESSBOOK_H
#define ADDRESSBOOK_H

#include <vector>
#include <memory>
#include "Contact.hpp"

/**
 * @class AddressBook
 * @brief Represents an address book that manages a collection of contacts.
 *
 * This class provides functionality to add, delete, search, and list contacts.
 * It uses a vector of shared pointers to manages contacts in different types.
 */

class AddressBook 
{
private:
    std::vector<std::shared_ptr<Contact>> contacts; ///< A vector of contacts.

public:
    /**
     * @brief Adds a contact to the address book.
     *
     * @param contact A shared pointer to the contact to be added.
     */
    void addContact(std::shared_ptr<Contact> contact);
    /**
     * @brief Deletes a contact from the address book by name.
     *
     * @param name The name of contact to be deleted.
     */
    void deleteContact(const std::string& name);
    /**
     * @brief Deletes all contacts from the address book.
     */
    void deleteAllContacts();
    /**
     * @brief Searches for a contact by name and display its details.
     *
     * @param name The name of the contact to search for.
     */
    void searchContact(const std::string& name) const;
    /**
     * @brief Lists all contacts in the address book.
     */
    void listContacts() const;
};

#endif // !ADDRESSBOOK_H