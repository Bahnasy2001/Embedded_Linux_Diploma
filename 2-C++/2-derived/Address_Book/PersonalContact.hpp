/**
 * @file PersonalContact.hpp
 * @brief Derived class for personal contacts in the address book.
 *
 * This file defines the `PersonalContact` class, which inherits from the base
 * `Contact` class and adds an additional attribute for the relationship with
 * the contact.
 */

#ifndef PERSONALCONTACT_H
#define PERSONALCONTACT_H

#include "Contact.hpp"
#include <string>

/**
 * @class PersonalContact
 * @brief Represents a personal contact in the address book.
 *
 * This class extends the functionality of the base `Contact` class by adding
 * an attribute for the relationship between the user and the contact.
 */

class PersonalContact : public Contact 
{
private:
    std::string relationship; ///< The relationship with the contact (e.g, friend, family).

public:
    /**
     * @brief Constructor to initialize a personal contact.
     *
     * @param name The name of the contact.
     * @param phoneNumber The phone Number of the contact.
     * @param relationship The relationship with the contact.
     */
    PersonalContact(const std::string& name, const std::string& phoneNumber, const std::string& relationship)
        : Contact(name, phoneNumber), relationship(relationship) {}
    /**
     * @brief Overrides the display method to include relationship information.
     */
    void display() const override
    {
        std::cout << "Name: " << name << ", Phone Number: "<< phoneNumber 
            << ", realtionship: " << relationship << std::endl;
    }
};

#endif // !PERSONALCONTACT_H
