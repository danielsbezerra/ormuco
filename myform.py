#!/usr/bin/env python

from wtforms import RadioField, Form, TextField, validators

class MyForm(Form):
    name = TextField('Name', validators=[validators.required()])
    favorite_color = TextField('Favorite Color')
    pet = RadioField('Cats or Dogs', choices=[('cat','Cat'),('dog','Dog')])