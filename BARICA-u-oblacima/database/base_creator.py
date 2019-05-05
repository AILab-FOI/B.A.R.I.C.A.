from database import app, db
from database.models import DBUser, DBRole

#for flask shell (must have .flaskenv):
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': DBUser, 'Role': DBRole}

#in normal prompt
#database creating: 
# flask db init
# flask db migrate -m "users table" ------> make migration script
# flask db upgrade -----------------------> execute migration script

#database changing:
#change User ORM class in models.py
# flask db migrate -m "users table" ------> make migration script
# flask db upgrade -----------------------> execute migration script

#run shell: 
# flask shell ----------------------------> start flask shell

#create Role (flask shell)
# r=Role(role="admin")
# db.session.add(r)
# db.session.commit()

#create User (flask shell)
# u=User(id=1,name="Barica") or User(name="Barica") ---------> auto increment id
# db.session.add(u)
# db.session.commit()

#list of all users (flask shell)
# users = User.query.all()
# users

#tables join
# users = User.query.join(Role, User.role_id==Role.id).add_columns(User.id,User.name,Role.role).all()
# users
# or: 
# for u in users:
#   print("{}: {} - {}".format(u.id,u.name,u.role))

#join renaming
# users = User.query.join(Role, User.role_id==Role.id).add_columns(User.id.label("uid"),User.name.label("uname"),Role.role.label("urole")).all()
# for u in users:
#   print("{}: {} - {}".format(u.uid,u.uname,u.urole))

#delete all (flask shell)
# User.query.delete() 
# db.session.commit()

#delete by attribute (flask shell)
# User.query.filter_by(id=5).delete()
# db.session.commit()

#delete by atribute - another way (flask shell)
# User.query.filter_by(id=5).one()
# db.session.delete(user)
# db.session.commit()

#get user by attribute (flask shell)
# user=User.query.filter_by(id=5).first()
# user=User.query.filter_by(name="Barica").first()
#also
# user=User.query.filter(User.name=="Barica").first()

#update password (flask shell)
# user = User.query.get(2)
#or
# user=User.query.filter_by(id=2).first()
# user.set_password("test")
# db.session.commit()

#check password
# user = User.query.get(2)
# user.check_password("best") ---------> False
# user.check_password("test") ---------> True

#in case of accident
#you can delete migrations folder but then you MUST upgrade revision table in app.db (sqlite3 database manager)
#see how to manage sqlite DBMS 
#or just delete app.db and create new one using flask db init - will create db and migrations folder




