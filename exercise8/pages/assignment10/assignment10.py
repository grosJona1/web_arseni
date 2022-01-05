from flask import Blueprint, render_template, redirect, url_for, request, session
from interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         template_folder='templates')


@assignment10.route('/assignment10')
def assignment10_fun():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert', methods=['POST'])
def insert_function():
    name = request.form['name']
    email = request.form['email']
    query = "insert into users(name, email) VALUES('%s', '%s');" % (name, email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')



@assignment10.route('/update_user', methods=['POST'])
def update_function():
    user_old_email = request.form['old_email']
    user_email = request.form['new_email']
    user_name = request.form['new_name']
    query = "UPDATE users SET email='%s', name='%s' WHERE email='%s';" % (user_email, user_name, user_old_email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@assignment10.route('/delete_user',  methods=['POST'])
def delete_function():
    user_email = request.form['email']
    query= "delete from users where email='%s';" % user_email
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

