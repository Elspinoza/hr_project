from config import db

"""Les types :
        Integer
        String(size)
        Text
        DateTime
        Float
        Boolean
        LargeBinary
        PickleType
""" 

"""Les proprietes cles des bdd:
        Primary_key
        nullable
        index
        unique

"""

class Employee(db.Model):

    #Creation de la table Employee avec ses attributs

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    firstName = db.Column(db.String(120), nullable = False)
    lastName = db.Column(db.String(120), nullable = False)

        #association [OneToMany]
    departmentId = db.Column(db.Integer, db.ForeignKey('department.id'), nullable = True)
    department = db.relationship('Department', foreign_keys = [departmentId])
        #association [OneToOne]
    isHeadOf = db.Column(db.Integer, db.ForeignKey('department.id'), nullable = True)
    manager = db.relationship('Department',foreign_keys = [isHeadOf])



class Department(db.Model):

    #Creation de la table department avec ses attributs

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)
    location = db.Column(db.String(120), nullable = False)
"""
    # #association 
    #     # OneToMany
    #     # /////backref cree une variable virtuel dans employee -------------- {Employee est la class}
    # employees = db.relationship('Employee', backref = 'depart')

     #OneToOne
    # head = db.relationship('Employee', backref = 'headOfDepartment')
"""

class Project(db.Model):

    #Creation de la table project avec ses attributs

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)


#ManyToMany

projectMembers= db.Table ('Project_members',
                db.Column('employee_id', db.ForeignKey('employee.id'), primary_key = True),
                db.Column('project_id', db.ForeignKey('project.id'), primary_key = True)
)

