from database import app, db
from database.models import DBUser

#for flask shell (must have .flaskenv):
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': DBUser}

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

#create User (flask shell)
# u=User(id=1,name="Barica") or User(name="Barica") ---------> auto increment id
# db.session.add(u)
# db.session.commit()

#list of all users (flask shell)
# users = User.query.all()
# u

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



