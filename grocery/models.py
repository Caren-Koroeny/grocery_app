from flask_login import UserMixin
from grocery import db

class User(UserMixin, db.Model):
    __tablename__ = "UsersTable"
    id = db.Column(db.Integer, primary_key = True)
    unique_id = db.Column(db.Integer, unique = True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    profile_pic = db.Column(db.String())
    
    
    
    def __repr__(self):
        return f'<User>{self.username, self.email, self.profile_pic}'
    
    def get_id(self):
        return self.unique_id
    
    
