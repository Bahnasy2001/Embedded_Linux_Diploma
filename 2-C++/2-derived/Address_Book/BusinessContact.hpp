/**
 * @file BusinessContact.hpp
 * @brief Derived class for business contacts in the address book.
 * 
 * This file defines the `BusinessContact` class, which inherits from the base
 * `Contact` class and adds an additional attribute for the company name.
 */
#ifndef BUSINESSCONTACT_H
#define BUSINESSCONTACT_H

#include "Contact.hpp"
#include <string>

/**
 * @class BusinessContact
 * @brief Represents a business contact in the address book.
 * 
 * This class extends the functionality of the base `Contact` class by adding
 * an attribute for the company name associated with the contact.
 */

class BusinessContact : public Contact
{
private:
    std::string company; ///< The company name associated with the contact.

public:
    /**
     * @brief Constructor to initialize a business contact.
     * 
     * @param name The name of the contact.
     * @param phoneNumber The phone number of the contact.
     * @param company The company name associated with the contact.
     */
    BusinessContact(const std::string& name, const std::string& phoneNumber, const std::string& company)
        : Contact(name, phoneNumber) , company(company) {}
    /**
     * @brief Overrides the display method to include company information.
     */
    void display() const override
    {
        std::cout << "Name: " << name << ", Phone Number: "<< phoneNumber 
            << ", company: " << company << std::endl;
    }

};

#endif // !BUSINESSCONTACT_H