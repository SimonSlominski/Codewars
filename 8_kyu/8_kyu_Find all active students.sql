/*  All tasks come from www.codewars.com

TASK: Find all active students

Create a simple SELECT query to display student information of all ACTIVE students.

    TABLE STRUCTURE:
    students
    Id	FirstName	LastName	IsActive

Note: IsActive (true or false)
*/

SELECT Id, FirstName, LastName FROM students WHERE IsActive;
