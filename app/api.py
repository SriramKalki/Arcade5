# this is one of my first times using REST oop
from flask import Blueprint, jsonify, request
from .models import Contact, db

api = Blueprint('api', __name__)

@api.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.to_dict() for contact in contacts])

@api.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return jsonify(contact.to_dict())

@api.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    new_contact = Contact(
        name=data.get('name'),
        email=data.get('email'),
        phone=data.get('phone')
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify(new_contact.to_dict()), 201

@api.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    data = request.get_json()
    contact.name = data.get('name', contact.name)
    contact.email = data.get('email', contact.email)
    contact.phone = data.get('phone', contact.phone)
    db.session.commit()
    return jsonify(contact.to_dict())

@api.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return '', 204

# Add this method to the Contact model in models.py
def to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'email': self.email,
        'phone': self.phone
    }

# Add this line to models.py under the Contact class
Contact.to_dict = to_dict