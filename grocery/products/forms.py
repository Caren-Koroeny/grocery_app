from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField, DateField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField

class ProductsForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    unit = StringField('Unit', [DataRequired()])
    price_per_unit = IntegerField('Price'), [DataRequired()]
    quantity = IntegerField('Quantity', [DataRequired()])
    discount = IntegerField('Discount', [DataRequired()])
    picture = FileField('Picture', [DataRequired])
    submit = SubmitField('Submit')
    
class ProductItemUpdateForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    unit = StringField('Unit', [DataRequired()])
    price_per_unit = IntegerField('Price'), [DataRequired()]
    quantity = IntegerField('Quantity', [DataRequired()])
    discount = IntegerField('Discount', [DataRequired()])
    picture = FileField('Picture', [DataRequired])
    pub_date = DateField('from', format='%Y-%m-%d')
    submit = SubmitField('Submit')
    
class GalleryUploadForm(FlaskForm):
    photo = FileField('Photo')
    submit = SubmitField('Upload')