# Employee management

#### Vision

Employee Management is a web based 
application for managing employees,
departments and vacation

**Application should provide:** 

    - Storing information about the employee's salary
    
    - Show employee list
   
    - Show list of departments
   
    - Updating the list of employees (adding, deleting, editing)
    
    - Show which department the employee belongs to



    
  
#### 1. Department 

This mode is intended for viewing the list of departments, the number of employees and the average salary.

##### 1.1 Display list of Clients

***Main scenario:***

     - User selects item “Department”;
     - Application displays list of departments
     
![](https://i.imgur.com/vzYIPyL.png)
   
***The list displays the following columns:***

    - Department - name of department
    
    - Salary - average salary by department
    
    - Amount - number of employees in the department

##### 1.2 Add department

***Main scenario:***

    - User clicks the "Add" button in the department list view mode
    
    - Application displays form to enter department data
    
    - User enter department data and presses "Save" button
    
    - If any data is entered incorrectly, incorrect data messages are displayed
    
    - If entered data is valid, then record is adding to database
    
    - If error occurs, then error message is displaying
    
    - If new department record is successfully added, then list of clients with added records is displaying
 
![](https://i.imgur.com/efBZOxO.png)
    
***Cancel operation scenario:***

    - User clicks the "Add" button in the department list view mode
    
    - Application displays form to enter department data
  
    - User enter department data and presses "Cancel" button
    
    - Data don’t save in data base, then list of department records is displaying to user
 
    
***When adding a department, the following details are entered:***

    - Name - name of department
    
***Constraints for data validation:***
  
After creating a new department, the average salary and the number of employees become 0

##### 1.3 Edit department

***Main scenario:***

    - User clicks the “Edit” button in the department list view mode
    
    - Application displays form to enter department data
    
    - User enters depatments data and presses “Save” button
    
    - If any data is entered incorrectly, incorrect data messages are displayed
    
    - If entered data is valid, then edited data is added to database
    
    - If error occurs, then error message is displaying
    
    - If the department record has been edited successfully, a list of departments with the added records is displayed
  
![](https://i.imgur.com/XTb3nmJ.png)
    
***Cancel operation scenario***

    - User clicks the “Edit” button in the departments list view mode
    
    - Application displays form to enter department data
    
    - User enters departments data and presses “Cancel” button
    
    - Data don’t save in data base, then list of clients records is displaying to user
    
##### 1.4 Removing department 

***Main scenario:***
    
    -  The user, while in the list of departments mode, presses the "Delete" button in the selected department line

    - Application displays confirmation dialog “Please confirm delete department?”
    
    - The user confirms the removal of the department
    
    - Record is deleted from database
    
    - If error occurs, then error message displays
    
    - If department record is successfully deleted, then list of department without deleted records is displaying
    
    - If there were people in this department, then they receive the mark "No department"
    
![](https://i.imgur.com/GOgLGa5.png)      
    
***Cancel operation scenario:***

    - User is in display mode of department list and press “Delete” button.
    
    - Application displays confirmation dialog “Please confirm delete department?”
    
    - User press “Cancel” button
    
    - List of departments without changes is displaying
     
    
#### 2. Employees 

##### 2.1 Display list if employee 

The mode is intended for displaying the list of employees, their salaries and department

***Main scenario:***

    - User selects item "Employees"
    
    - Application display a list of employees

![](https://i.imgur.com/jtvC6FK.png)     
   
**The list displays the following columns:**
    
    - Employee - employee name
    
    - Department - employee department
    
    - Salary - average employee salary
    
    - Position - employee's position
    
    - Date - date of hiring
    
##### 2.2 Add employee

***Main scenario:***

    - User clicks "add" button in employee view

    - Application displays form to enter order data

    - User enters employee data and presses "Save" button

    - If entered data is valid, then record is adding to database

    - If error occurs, then error message is displaying

    - If the employee is successfully added, then his data is displayed in the employee view mode

![](https://i.imgur.com/EQM6I01.png)    

***Cancel operation scenario:***

    - User clicks the “Add” button in the employee list view mode
    
    - Application displays form to enter employee data
    
    - User enters employee data and presses “Cancel” button
    
    - Data don’t save in data base, then list of employee records is displaying to user
  
    
**When adding a employee, the following details are entered:**

    - Name - employee name
    
    - Department - employee department
    
    - Salary - average employee salary
    
    - Position - employee's position
    
    - Date - date of hiring
    
##### 2.3 Edit list of employees
***Main scenario:***

    - User clicks the “Edit” button in the employee list view mode
    
    - Aplication display form to enter employee data
    
    - User enters emloyee data and presses “Save” button
    
    - If any data is entered incorrectly, incorrect data messages are displayed
    
    - If entered data is valid, then record is adding to database
    
    - If error occurs, then error message is displaying
    
    - If new employee record is successfully added, then list of employees with added records is displaying
    
![](https://i.imgur.com/PT5HrVv.png)

***Cancel operation scenario:***

    - User clicks the “Edit” button in the employee list view mode
    
    - Application displays form to enter employee data
    
    - User enters employee data and presses “Cancel” button
    
    - Data don’t save in data base, then list of employee records is displaying to user

   
**When editing a employee, the following details are entered:**
    
    - Name - employee name
    
    - Department - employee department
    
    - Salary - average employee salary
    
    - Position - employee's position
    
    - Date - date of hiring
    
***Constraints for data validation:***

    - Name - maximum length 50 characters
    
    - Department - maximum length 50 characters
    
    - Salary - minimum salary 1$
    
    - Position - maximum length 50 characters
    
    - Date - date of addition to the employee in dd / mm / yyyy format
    
##### 2.4 Removing the employee

***Main scenario:***

    - The user, being in the list of employees, clicks the "Delete" button in the selected order line

    - If the employee can be removed, a confirmation dialog is displayed
    
    - the user confirms the deletion of the employee
    
    -  Record is deleted from database
    
    - If error occurs, then error message displays
    
    - If employee record is successfully deleted, then list of employees without deleted records is displaying

![](https://i.imgur.com/VhJlIWg.png)
   
***Cancel operation scenaria:***
    
    - User is in display mode of employees list and press “Delete” button;
  
    - Application displays confirmation dialog “Please confirm delete employee?”;
  
    - User press “Cancel” button;
  
    - List of employees without changes is displaying.
     
    
#### 3. Vacation

##### 3.1 Display vacation list

This mode is intended for viewing employees on vacation, deleting and editing the vacation date

**Main scenario:** 

    - User select item "Vacation"
    
    - Application display vacation list
    
![](https://i.imgur.com/yqPVrA2.png)    
    
**This list displays the following columns:**

    - Employee - employee name
    
    - Start - vacation start
    
    - End - end of vacation
    
##### 3.2 Add vacation 

**Main scenario:**  

    - User clicks the "Add" button in the vacation list view mode
    
    - Application display form to enter vacation data
    
    - User enters vacation data and presses "Save" button
    
    - If any data is entered incorrectly, incorrect data messages are displayed
    
    - If entered data is valid, then record is adding to database
    
    - If error occurs, then error message is displaying
    
    - If new client record is successfully added, then list of vacation with added records is displaying

![](https://i.imgur.com/RpfP5ve.png)
    
**Cancel operation scenario:**

    - User clicks the “Add” button in the vacation list view mode
    
    - Application displays form to enter vacation data
    
    - User enters vacation data and presses “Cancel” button
    
    - Data don’t save in data base, then vacation records is displaying to user

   
**When adding a vacation, the following details are entered:**

    - Name - employee name
    
    - Start - vacation start
    
    - End - vacation end 
    
**Constraints for data validation:**
    
    - Name – maximum length of 30 characters
    
    - Start – vacation registration date in format dd/mm/yyyy
    
    - End – vacation registration date in format dd/mm/yyyy
    
##### 3.3 Edit vacation 

**Main scenario:**
    
    - User clicks the “Edit” button in the vacation list view mode
    
    - Application displays form to enter vacation data
    
    - User enters vacation data and presses “Save” button
    
    - If any data is entered incorrectly, incorrect data messages are displayed
    
    - If entered data is valid, then edited data is added to database
    
    - If error occurs, then error message is displaying
    
    - If vacation record is successfully edited, then list of vacation with added records is displaying

![](https://i.imgur.com/qLrEXJg.png)
    
**Cancel operation scenario:**

    - User clicks the “Edit” button in the vacation list view mode
    
    - Application displays form to enter vacation data
    
    - User enters vacation data and presses “Cancel” button
    
    - Data don’t save in data base, then list of vacation records is displaying to user

   
##### 3.4 Removing vacation

**Main scenario:**
    
    - The user, while in the list of vacation mode, presses the "Delete" button in the selected vacation line
    
    - Application displays confirmation dialog “Please confirm delete vacation?”
    
    - The user confirms the removal of the vacation
    
    - Record is deleted from database
    
    - If error occurs, then error message displays
    
    - If client record is successfully deleted, then list of vacation without deleted records is displaying

![](https://i.imgur.com/gJtX9af.png)
   
**Cancel operation scenario:**

    - User is in display mode of vacation list and press “Delete” button
    
    - Application displays confirmation dialog “Please confirm delete vacation?”
    
    - User press “Cancel” button
    
    - List of vacations without changes is displaying
    

