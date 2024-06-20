from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Contact, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@main.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        new_contact = Contact(name=name, email=email, phone=phone)
        db.session.add(new_contact)
        db.session.commit()
        flash('Contact added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_contact.html')