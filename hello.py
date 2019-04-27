# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World'

# @app.route('/index')
# def index_page():
#     return 'This is a index page'

# @app.route('/homepage')
# def home_page():
#     return "this is a home page"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath


# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

from flask import Flask, url_for, request, render_template, make_response
from flask import abort, redirect, session, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# sys.path.append("scr")


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return "hey man, this is 404 customized", 404


@app.route('/error')
def this_does_error():
    abort(404)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "login_done"
    else:
        return "showing you the form"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        response = make_response(render_template('hello.html', name=name))
        flash('you were successfully logged in')
        session['username'] = name
        return response
    else:
        if 'username' in session:
            return render_template('hello.html', name=session['username'])
        else:
            return render_template('hello.html', name='no user')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file_to_elastic_search():
    if request.method == 'POST':
        return "file upload successful"
    else:
        return render_template('upload_file.html')



with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe', next='/', nextofnext='//'))
    print(url_for('static', filename='style.css'))

