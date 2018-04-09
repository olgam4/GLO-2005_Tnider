from flask import Flask, render_template, flash, request, g, redirect
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from persistance.passwordUtil import hash_password, check_password
from Users import *
import pymysql
from itsdangerous import URLSafeTimedSerializer
from LoginForm import LoginForm
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY="allo key",
    REMEMBER_COOKIE_DURATION=timedelta(days=7)
))

login_manager = LoginManager()
login_serializer = URLSafeTimedSerializer(app.secret_key)



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/browse')
def browse():
    return render_template('browse.html')


@app.route('/account')
def sign_in():
    return render_template('account.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/account-preferences')
def account_preferences():
    return render_template('account-preferences.html')

@app.route('/account-transactions')
def account_transactions():
    return render_template('account-transactions.html')

@app.route('/account-info')
def account_info():
    return render_template('account-info.html')


@app.route("/", methods=["GET", "POST"])
def login_page():
    form = LoginForm(request.form)
    if request.method == "POST":
        user = User.get(form.email.data)
        # If we found a user based on username then compare that the submitted
        # password matches the password in the database.  The password is stored
        # is a slated hash format, so you must hash the password before comparing
        # it.

        print("test sandy")
        if user and check_password(user.password, form.password.data):
            print("henlo this is birb")
            login_user(user, remember=True)

            return redirect(request.args.get("next") or "/")

    return render_template("home.html")


@app.route("/logout/")
def logout_page():
    logout_user()
    return redirect("/")


def get_db():
    if not hasattr(g, 'cursor'):
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             autocommit=True)

        g.cursor = db.cursor(pymysql.cursors.DictCursor)
        g.cursor.execute("USE PROJET_BD")
       # print("Cursor generated \n")
    return g.cursor


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'cursor'):
        g.cursor.close()


@login_manager.user_loader
def load_user(email):
    return User.get(email)


@app.route("/restricted/")
@login_required
def restricted_page():
    user_id = (current_user.get_id() or "No User Logged In")
    return render_template("restricted.html", user_id=user_id)


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run(debug=True)
