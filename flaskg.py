from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('Name:',validators=[DataRequired()])
    pwd = PasswordField('Passwords:',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    email = None
    pwd = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        pwd = form.pwd.data
    return render_template('index.html',form=form, name=name,email=email,passwords=pwd)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



app.config['SECRET_KEY']="hard to guess string"

if __name__ == '__main__':
    app.run(debug=True)
