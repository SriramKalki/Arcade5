from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Contact, db
from .forms import ContactForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@main.route('/add', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(name=form.name.data, email=form.email.data, phone=form.phone.data)
        db.session.add(new_contact)
        db.session.commit()
        flash('Contact added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_contact.html', form=form)

@main.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = Contact.query.get(contact_id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.email = form.email.data
        contact.phone = form.phone.data
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit_contact.html', form=form)

@main.route('/delete/<int:contact_id>')
def delete_contact(contact_id):
    contact = Contact.query.get(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('main.index'))