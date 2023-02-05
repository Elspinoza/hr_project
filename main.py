from app import app
from config import db
from models import Employee, Department, Project
from flask import Flask, request, jsonify
from flask_cors import CORS

#db.app_context().push()

with app.app_context():
    db.create_all()

    department1 = Department(name = "Bijou", location = "Lome")
    department2 = Department(name = "Bijoujou", location = "Lome2")
    department3 = Department(name = "Bijoujoul", location = "Lome3")

    employee1 = Employee(firstName = "BETA", lastName = "ALPHA", department = department1)
    employee2 = Employee(firstName = "RAPHA", lastName = "OMEGA")
    employee3 = Employee(firstName = "RAPHAtee", lastName = "OMEGAs")

    db.session.add(department1)
    db.session.add(department2)
    db.session.add(department3)
    db.session.add(employee1)
    db.session.commit()

"""Methode et route"""

#======================================================POST===============================================


#Methode d'ajout employe

@app.route('/employee/add', methods=['POST'])
def add_employee():
    try:
        json = request.json
        firstName = json['firstName']
        lastName = json['lastName']
        departmentId = json['departmentId']
        
        if  firstName and lastName and request.method == 'POST':
            employee = Employee(firstName = firstName, lastName = lastName)
            if departmentId :
                department = Department.query.filter_by(id=departmentId).first()
                print(department)
                employee.department = department
            db.session.add(employee)
            db.session.commit()
            resultat = jsonify('Employe ajoute')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()
    

#Methode d'ajout department

@app.route('/department/add', methods=['POST'])
def add_department():
    try:
        json = request.json
        name = json['name']
        location = json['location']

        if  name and location and request.method == 'POST':
            department = Department(name = name, location = location, employees = [])
            db.session.add(department)
            db.session.commit()
            resultat = jsonify('Departement ajoute')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#Methode d'ajout de project

@app.route('/project/add', methods=['POST'])
def add_project():
    try:
        json = request.json
        name = json['name']

        if  name and request.method == 'POST':
            project = Project(name = name)
            db.session.add(project)
            db.session.commit()
            resultat = jsonify('Project ajoute')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

#======================================================GET===============================================

#Methode GET pour Employee

@app.route('/employees', methods = ['GET'])
def get_all_employee():
    try:
        employees = Employee.query.all()
        data = [{"id":employee.id,"firstName":employee.firstName, "lastName":employee.lastName} for employee in employees]

        resultat = jsonify({"status_code": 200, "Employee" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

#Methode GET pour department

@app.route('/departments', methods = ['GET'])
def get_department():
    try:
        departments = Department.query.all()
        data = [{"id":department.id,"location":department.location} for department in departments]

        resultat = jsonify({"status_code": 200, "Employee" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()

#Methode GET pour project

@app.route('/projects', methods = ['GET'])
def get_project():
    try:
        projects = Project.query.all()
        data = [{"id":project.id,"name":project.name} for project in projects]

        resultat = jsonify({"status_code": 200, "Employee" : data})

        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status" : 404, "message" : 'Error'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#======================================================DELETE===============================================

@app.route('/employee/delete/', methods=['POST'])
def delete_employee():
    try:
        json = request.json
        id = json['id']
        employee = Employee.query.filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()
        resultat = jsonify('employe supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/department/delete/', methods=['POST'])
def delete_department():
    try:
        json = request.json
        id = json['id']
        department = Department.query.filter_by(id=id).first()
        db.session.delete(department)
        db.session.commit()
        resultat = jsonify('department supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/project/delete/', methods=['POST'])
def delete_project():
    try:
        json = request.json
        id = json['id']
        project = Project.query.filter_by(id=id).first()
        db.session.delete(project)
        db.session.commit()
        resultat = jsonify('project supprimé ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return resultat
    finally:
        db.session.rollback()
        db.session.close()


#======================================================UPDATE===============================================

@app.route('/employee/update/', methods=['POST', 'GET'])
def update_employee():
    try:
        data = request.json
        id = data["id"]
        firstName = data["firstName"]
        lastName = data["lastName"]
        employee = Employee.query.filter_by(id=id).first()
        if id and firstName and lastName and request.method == 'POST':
            employee.firstName = firstName
            employee.lastName = lastName
            db.session.commit()
            resultat = jsonify('Employee mise à jour')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/department/update/', methods=['POST', 'GET'])
def update_department():
    try:
        data = request.json
        id = data["id"]
        name = data["name"]
        location = data["location"]
        department = Department.query.filter_by(id=id).first()
        if id and name and location and request.method == 'POST':
            department.name = name
            department.location = location
            db.session.commit()
            resultat = jsonify('Employee mise à jour')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()


@app.route('/project/update/', methods=['POST', 'GET'])
def update_project():
    try:
        data = request.json
        id = data["id"]
        name = data["name"]
        project = Project.query.filter_by(id=id).first()
        if id and name and request.method == 'POST':
            project.name = name
            db.session.commit()
            resultat = jsonify('Employee mise à jour')
            return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()





if(__name__ == '__main__'):
    app.run()