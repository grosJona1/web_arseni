from flask import Flask, redirect, url_for, render_template, request #query parameters
from flask import session
from interact_with_DB import interact_db


app = Flask(__name__) # we will work on one instanse of the class Flask
app.secret_key = '1234' # this is for session, flask demands encryption


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
def logout_fun():
    session['user'] = ""
    session['userinside'] = False
    return render_template('Logout.html')


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run(debug=True)
