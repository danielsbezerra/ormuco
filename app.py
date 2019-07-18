#!/usr/bin/env python

from flask import Flask, escape, request, flash, render_template
from myform import MyForm
import secrets, data_access

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/", methods=['GET', 'POST'])
def root():
    form_values = MyForm(request.form)

    # create a database connection
    db_file='./demo.db'
    conn = data_access.create_connection(db_file)

    if form_values.validate():
        try:
            #import ipdb; ipdb.set_trace() # the same as breakpoint()
            data = (form_values.name.data, form_values.favorite_color.data, form_values.pet.data)
            data_access.insert_preference(conn, data)
            flash('Preference inserted.')
        except Exception as e:
            flash('Failed to insert preference.')
            return str(e), 500
    elif request.method=='POST':
        flash('All the form fields are required. ')

    #import ipdb; ipdb.set_trace() # the same as breakpoint()
    all_preferences = data_access.select_all_preferences(conn)

    return render_template('root.html', form=form_values, **{'all_preferences':all_preferences})


if __name__ == "__main__":
    app.run()
