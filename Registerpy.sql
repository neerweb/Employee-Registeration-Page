CREATE DATABASE registerpy;

USE registerpy;

CREATE TABLE Employee (
    EmpCode INT PRIMARY KEY IDENTITY(1,1),
    EmpName VARCHAR(100),
    EmpAdd VARCHAR(255),
    EmpMobile VARCHAR(15),
    EmpEmail VARCHAR(100),
    Designation VARCHAR(50),
    Department VARCHAR(50),
    UserID VARCHAR(50) UNIQUE,
    Password VARCHAR(255)
);
