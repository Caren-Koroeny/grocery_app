from crypt import methods
from itertools import product
import os
# import secrets
from PIL import Image
from flask import Blueprint,flash, redirect, render_template, request, session, url_for
from grocery.models import ProductItems
from grocery.products.forms import ProductsForm, ProductItemUpdateForm
from grocery import db, create_app

basedir = os.path.abspath(os.path.dirname(__file__))

products = Blueprint('product', __name__)

app = create_app()


# CRUD....


# create
@products.route('/create/product/item', methodst=['GET', 'POST'])
def create_product_item():
    product = ProductItems()
    form = ProductsForm()
    
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.add(product)
        db.session.commit()
        flash(f'Welcome admin......', 'success')
        return redirect(url_for('products.products_list_view'))
    return render_template('/products/create_product.html', form=form)

#Retreive products
@products.route("/item/list", methods=["POST", "GET"]) 
def product_list_view():
    product = ProductItems.query.all()
    return render_template('/products/product_list.html', product=product)

# Update

# Delete

# save image..