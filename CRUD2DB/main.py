from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import text
import traceback
from core.database import SessionLocal, engine
from utils import *
# from models import *
# from typing import Annotated

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  way 1 to write parameterized sql query
@app.post("/add_employee/")
async def add_employee(name: str, email: str, position: str, db: Session = Depends(get_db)):
    try:
        query = f'''
                    INSERT INTO employee (name, email, position) 
                    VALUES ('{name}', '{email}', '{position}');
                '''
        db.execute(text(query))
        db.commit()
        # return {'name' : name, 'email': email, 'position' : position}
        output_json = await output_json_creator(('name', 'email', 'position'), ((name, email, position)))
        return output_json
        

    except Exception as e:
        print('ERROR FOUND')
        # traceback.print_exc('_____EXCEPTION_____ : ', e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/list_employees/')
async def list_employees(db: Session = Depends(get_db)):
    try:
        query = f"""
                    SELECT * 
                    FROM employee;
                """
        result = db.execute(text(query))
        employees = result.fetchall()
        if employees:
            output_json = await output_json_creator(('id', 'name', 'email', 'position'), employees)
            return output_json
            # return [{'id': employee[0], 'name': employee[1], 'email': employee[2], 'position': employee[3]} for employee in employees]
        else:
            raise HTTPException(status_code=404, detail='Employees not found')

    except Exception as e:
        print('ERROR FOUND')
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/get_employee/{id}')
async def get_employee(id: int, db:Session = Depends(get_db)):
    try:
        query = f"""
                    SELECT * 
                    FROM {employee} 
                    WHERE id = {0};
                """.format(id)
        print(query)
        result = db.execute(text(query))
        employee = result.fetchone()
        if employee:
            # employee_dict = {
            #     'id': employee[0],
            #     'name': employee[1],
            #     'email': employee[2],
            #     'position': employee[3]
            # }
            # return employee_dict
            output_json = await output_json_creator(('id', 'name', 'email', 'position'), employee)
            return output_json
        else:
            raise HTTPException(status_code=404, detail='Employee not found')

    except Exception as e:
        print('ERROR FOUND')
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.put('/update_employee/{id}')
async def update_employee(id:int, name:str, email: str, position: str, db: Session = Depends(get_db)):
    try:
        query = f"""
                    UPDATE employee 
                    SET name = '{name}', email = '{email}', position = '{position}' 
                    WHERE id = {id};
                """
        result = db.execute(text(query))
        db.commit()
        if result.rowcount != 0:
            output_json = await output_json_creator(('id', 'name', 'email', 'position'), ((id, name, email, position)))
            return output_json
            # return {'id': id, 'name' : name, 'email': email, 'position' : position}
        else:
            raise HTTPException(status_code=404, detail='Employee not found')
        
    except Exception as e:
        print('ERROR FOUND')
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete('/delete_employee/{id}')
async def delete_employee(id: int, db: Session= Depends(get_db)):
    try:
        query = f"""
                    DELETE FROM employee
                    WHERE id = {id};
                """
        db.execute(text(query))
        db.commit()
        return {'message': 'Employee deleted successfully'}
    
    except Exception as e:
        print('ERROR FOUND')
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

