# Password Generator

This is a simple password generator program implemented in Python.

## Description

This program generates strong and secure passwords of variable lengths based on user input. It utilizes a combination of lowercase letters, uppercase letters, numbers, and special characters to create passwords that are difficult to guess or crack.

## Features

- Customizable password length
- Options to include or exclude uppercase letters, lowercase letters, numbers, and special characters
- Generates passwords using a secure random generator
- Easy-to-use command-line interface

## Waterfall Model
 
1. Requirements Phase:

Purpose: The purpose of the program is to generate random passwords based on user-defined criteria.
User Requirements:
User should be able to specify the length of the password.
User should have the option to include or exclude uppercase letters, lowercase letters, digits, and special characters in the generated password.

2. Design Phase:

Architecture:
The program consists of two main functions: generate_password() and main().
generate_password() is responsible for generating passwords based on user-defined criteria.
Flow:
main() function prompts the user to input the password length and character inclusion preferences.
User input is collected and passed to generate_password() function.
generate_password() constructs the password based on the specified criteria and returns it to main().

3. Implementation Phase:

Coding Standards: The code follows Python coding standards and conventions for readability and maintainability.
Error Handling: The program handles invalid input gracefully by catching ValueError exceptions and displaying appropriate error messages.

4. Testing Phase:

Unit Testing: Each function (generate_password() and main()) can be tested individually to ensure they work as expected.
Integration Testing: The program can be tested as a whole to verify that the components interact correctly and produce the desired output.
Validation Testing: Test the program with various input scenarios to validate that it meets user requirements.

5. Deployment Phase:

Packaging: Prepare the program for distribution, ensuring all necessary files and dependencies are included.
Documentation: Provide documentation on how to install and use the program, including instructions on specifying password criteria and interpreting the generated passwords.

6. Maintenance Phase:

Bug Fixes: Address any issues or bugs reported by users post-deployment.
Updates: Incorporate updates or enhancements based on user feedback or changing requirements.
Support: Provide ongoing support to users and address any queries or concerns they may have.


## Installation

1. Clone the repository:

```bash
git https://github.com/jt1402/Password-generator.git 
