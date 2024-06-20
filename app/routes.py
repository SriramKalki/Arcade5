from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

contacts = []

@main.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@main.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        contacts.append({'name': name, 'email': email, 'phone': phone})
        return redirect(url_for('main.index'))
    return render_template('add_contact.html')