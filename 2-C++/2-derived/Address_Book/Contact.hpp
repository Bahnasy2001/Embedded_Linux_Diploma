/** 
 * @file Contact.hpp
 * @brief Base class for all types of contacts in the address book.
 *
 * this file defines the base class `Contact`, which provides common functionality
 * for all contact types. It includes attributes such as name and phone Number,
 * along with methods to display contact information.
 */

#ifndef CONTACT_H
#define CONTACT_H

#include <string>
#include <iostream>

/**
 * @class Contact
 * @brief Represents a generic contact in the address book.
 *
 * This class serves as the base class for all contact types. It stores basic
 * information about a contact, such as their name and phone Number, and provides
 * a virtual method for displaying contact details.
 */

class Contact 
{
protected:
    std::string name; ///< The name of the contact.
    std::string phoneNumber; ///< The phone number of the contact.

public:
    /**
     * @brief Constructor to intialize a contact with a name and phone Number.
     * 
     * @param name The name of the contact.
     * @param phoneNumber The phone number of the contact.
     */
    Contact(const std::string& name, const std::string& phoneNumber)
        : name(name), phoneNumber(phoneNumber) {}

    /**
     * @brief Virtual destructor to ensure proper cleanup of derived classes.
     */
    virtual ~Contact() = default;
    /**
     * @brief Displays the contact's details.
     * 
     * This method is overriden by drived classes to provide specific
     * implementations for different types of contacts.
     */
    virtual void display() const 
    {
        std::cout << "Name: " <<name << ", Phone Number: " << phoneNumber << std::endl;
    }
    /**
     * @brief Gets the name of contact.
     * 
     * @return std::string the name of contact.
     */
    std::string getName() const 
    {
        return name;
    }
};

#endif // !CONTACT_H
