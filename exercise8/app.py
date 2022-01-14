from flask import Flask, redirect, url_for, render_template, request
from flask import session
from flask import jsonify
import random
import requests
from interact_with_DB import interact_db


app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def cv():
    return render_template('CV1.html')


@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
                           name='YONI GROSSMAN',
                           hobbies=('football', 'basketball', 'yoga'),
                           account='guest')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    # this is my Data Base
    users = {'Michael_Jordan@gmail.com': {'name': 'Michael Jordan', 'email': 'Michael_Jordan@gmail.com'},
             'Tom_Brady@gmail.com': {'name': 'Tom Brady', 'email': 'Tom_Brady@gmail.com'},
             'Deni_Avdija@gmail.com': {'name': 'Deni Avdija', 'email': 'Deni_Avdija@gmail.com'},
             'Avi_Nimni@gmail.com': {'name': 'Avi Nimni', 'email': 'Avi_Nimni@gmail.com'},
             'Ofer_Levi@gmail.com': {'name': 'Ofer Levi', 'email': 'Ofer_Levi@gmail.com'}}

    # if user enter Empty Submit
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']
            return render_template('assignment9.html', email=email, users=users)

        # Direct from URL
        return render_template('assignment9.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # insert to users name & email
        session['user'] = name
        session['userinside'] = True
        return redirect(url_for("assignment9"))


@app.route('/Logout')
def logout():
    session['user'] = ""
    session['userinside'] = False
    return render_template('Logout.html')


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route('/assignment11')
def assignment11():
    return render_template('assignment11.html')


@app.route('/assignment11/users')
def assignment11_users():
    return_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        return_dict['user'] = {
            'status': 'The operation was successful',
            'id': user.id,
            'name': user.name,
            'email': user.email,
        }
    return jsonify(return_dict)


@app.route('/assignment11/outer_source')
def assignment11_outer_source():
    return render_template('outer_source.html')


def get_user(id):
    if (id != ""):
        user_id = int(id)
        return requests.get(f'https://reqres.in/api/users/{user_id}').json()

    users = []
    length = len(requests.get(f'https://reqres.in/api/users').json()['data'])

    for i in range(1, length+1):
        res = requests.get(f'https://reqres.in/api/users/{i}')
        res = res.json()
        users.append(res)
    return users


@app.route('/req_backend')
def request_backend():
    if "user_id" in request.args:
        user_id = request.args['user_id']
        if user_id == "":
            users = get_user(user_id)
            return render_template('outer_source.html', users=users)
        else:
            user = get_user(user_id)
            return render_template('outer_source.html', user=user)

    return render_template('outer_source.html')



if __name__ == '__main__':
    app.run(debug=True)
