Capstone 01: Python Project for Purwadhika

In this project, I've developed a mini application for managing the Customer Database of PT ABC Investment Capital. 
There are six menus available for users to navigate. 
However, before accessing any menu, the system prompts users to enter their username and password to recognize their team affiliation. 
I've organized users into three teams, each with different access levels:

1. General Manager: They have access to all menus.
2. Relations Team: This team can access menu 1 to read data and menu 5 to update priority customer information.
   However, they are restricted from adding or making changes to the data.
3. Data Team: Members of this team can access all menus except menu 4, where they cannot delete any data.
If users input the wrong username and password, they will be prompted to try again until they provide the correct credentials.

Here's a breakdown of the menus:

Menu 1 - Read Customer Database
1.1: View the overall customer database.
1.2: Look up a specific customer by their ID or identity card number.
1.3: Return to the main menu.

MENU 2 - Add Customer to the Database
2.1 Add Customer
In this section, before users input new information, the system checks whether the customer's identity card number is already in the system or not.
- If the customer's identity card number is already in the system, they will be returned to Menu 2, and the system will notify them that the data already exists.
- If the customer's identity card number is not yet in the system, they will go through a series of inputs to add new data.
  
In this section, the system is designed to generate a unique ID for the company's identification for each customer.
The unique ID is created based on the year and month of data creation, the month and date of their birth, and the sum of their name's index number position.

After users input all the data, the system displays an overview and asks for confirmation if there are any changes they would like to make. 
If they confirm, they can choose based on the column and make specified changes. 
This loop continues until the user types 't', indicating they have confirmed the data is correct

2.2 Back to main menu


MENU 3 - Update database customer 
3.1 Change data customer
- Users enter a customer's ID; if it's not in the system, they are notified and returned to Menu 3.
- Upon entering a matching customer ID, users can update customer data similar to Menu 2.
- Users are prompted to confirm changes before they are saved.
  
3.2 Back to main menu

MENU 4 - Delete Data
4.1 Delete Data
In this section, the overall system operates similarly to Menu 2 and Menu 3, where the user will be prompted to input the customer's ID. 
Once inputted, the system displays the corresponding data and then asks if the user is sure they want to proceed with deletion.
If the user confirms by selecting 'yes', the data will be deleted from the system. 
And then there will be table that displays all the data to confirm that the removed data has been successfully deleted from the system.

4.2 Back to main menu

MENU 5 - PRIORITY CUSTOMER
In Menu 5, we focus on identifying priority customers, who are defined as those having funds exceeding 750 million IDR and holding priority status.

5.1 Priority Relationship
This section showcases customers who have birthdays in the same month the user accesses the menu. 
For instance, if the user selects this menu on February 28, 2024, the system will display customers celebrating birthdays in that month. 
If there are birthday customers, their data will be presented. However, if no customers have birthdays in that month, the system will notify the user accordingly.

5.2 Priority Target
This feature filters customers with funds exceeding 750 million IDR but have not yet been granted priority status. 
It's designed to assist the relations team in identifying potential targets for their efforts.

5.3 Priority Customer
In contrast to Menu 5.2, this section displays customers who have already been classified as priority due to meeting the defined criteria. 
It serves as a reference for the team to track the current priority customers.

These options within Menu 5 provide valuable insights into the customer base, helping teams effectively prioritize their interactions and focus their efforts 
on high-value clients

6. SIgn out
After signing out, they will be redirected to the sign-in menu for further actions.
