from sqlalchemy import String, Integer, Boolean, Column
from sqlalchemy.ext.declarative import declarative_base
# from database import Base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee' 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    position = Column(String(255))

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    company_name = Column(String(255))


# # Creating tables in mysql query

# CREATE TABLE employeemanagement.company (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     email VARCHAR(255),
#     position VARCHAR(255)
# );

# CREATE TABLE company (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     employee_id INT,
#     company_name VARCHAR(255),
#     FOREIGN KEY (employee_id) REFERENCES employee(id)
# );