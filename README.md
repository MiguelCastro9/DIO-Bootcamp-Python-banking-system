# Overview - bank-v2

Create a banking system with operations: withdraw, deposit and view statements.


### Challenge

We need to make our code more modularized, to do this we will create functions for existing operations: withdraw, deposit and view history. Furthermore, for version 2 of our system we need to create two new functions: create user (bank customer) and create current account (link with user).

### Separations in functions

We must create functions for all system operations, to exercise everything we learned in this module, each function will have a rule for passing arguments. The return and the way they will be called can be defined by you as you see fit.

### Withdraw

The withdrawal function must receive arguments only by name (keyword only). Suggested arguments: balance, value, statement, limit, number_withdrawals, limit_withdrawals. Return suggestion: <code>balance</code> and <code>statement</code>.

### Deposit

The deposit function must receive arguments only by positional only. Suggested arguments: balance, value, statement. Return suggestion: balance and statement.

### Extract

The extract function must receive arguments by position and name (positional only and keyword only). Positional arguments: balance, named arguments: extract.

### New functions

We need to create two new functions: create user and create current account. Feel free to add more functions, for example: list accounts.

### Register user (client)

The program must store users in a list, a user consists of: name, date of birth, social security number and address. The address is a string with the format: street, number - neighborhood - city/state acronym. Only CPF numbers must be stored. We cannot register 2 users with the same CPF.

### Register current account

The program must store accounts in a list, an account is composed of: agency, account number and user. The account number is sequential, starting from 1. The branch number is fixed: "0001". A user can have more than one account, but an account belongs to only one user.

### Demo

https://github.com/MiguelCastro9/DIO-Bootcamp-Python-banking-system/assets/56695817/41ff20d3-4fd1-4053-9e5f-fbbcecc93a36

<br><br>

# Overview - bank-v1

Create a banking system with operations: withdraw, deposit and view statements.


### Challenge

We were hired by a large bank to develop their new system. This bank wants to modernize its operations and for this I chose the Python language. 
For the first version of the system we must implement only 3 operations: deposit, withdrawal and statement.

### Deposit Operation

It must be possible to deposit positive amounts into my bank account. v1 of the project only works with 1 user, so we don't need to worry about identifying the branch and 
bank account number. All deposits must be stored in a variable and displayed in the statement operation.

### Withdrawal Operation

The system must allow you to make 3 daily withdrawals with a maximum limit of R$500.00 per withdrawal. 
If the user does not have a balance in their account, the system must display a message stating that it will not be possible to withdraw the money due to lack of balance. 
All withdrawals must be stored in a variable and displayed in the statement operation.


### Extract Operation

This operation must list all deposits and withdrawals made to the account. At the end of the list, the current account balance should be displayed. 
If the statement is blank, display the message: No transactions were carried out. The values must be displayed using the format R$ xxx.xx, example: 1500.45 = R$ 1500.45

### Demo

https://github.com/MiguelCastro9/DIO-Bootcamp-Python-banking-system/assets/56695817/adadb2b0-cc16-401b-b390-a0f28c9208e1

