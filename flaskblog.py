from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '8377a42f30d37efd9dc260fc46feb2cf'
posts = [
    {
        'author': 'Bernard Palabasan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 01, 2022'
    },
    {
        'author': 'john Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 02, 2022'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')
    
@app.route('/register')
def register():
    form =  RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/register')
def register():
    form =  LoginForm()
    return render_template('login.html', title='Login', form=form)

# this is for debug mode no need to close terminal
# refresh refresh lang sa browser ganern!
if __name__ == '__main__':
    app.run(debug=True)