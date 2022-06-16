from datetime import datetime
from this import d
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
    


class ProductItems(db.Model):
    __tablename__ = 'productlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    unit = db.Column(db.String(10), nullable=False, unique=False)
    price_per_unit = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, default=0)
    quantity = db.Column(db.Integer)
    picture = db.Column(db.String(), default='defaul.jpg')
    pub_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    
    
    def __repr__(self):
        return f'<Product> {self.id, self.name, self.unit, self.price_per_unit,self.discount, self.quantity, self.picture,self.pub_date}'
    



class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String())        
    
