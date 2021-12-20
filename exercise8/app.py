from flask import Flask, render_template


app= Flask(__name__)

@app.route('/')
def cv():
    return render_template('CV1.html')

@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',
                           name = 'YONI GROSSMAN',
                           hobbies=('football' ,'basketball', 'yoga'),
                           account='guest')


if __name__ == '__main__':
    app.run(debug=True)