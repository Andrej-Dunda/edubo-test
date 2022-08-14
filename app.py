from flask import Flask, render_template, request, session, redirect, url_for, g
from flask_mail import Mail, Message
from new_passw import generate_random_password
from user_handler import update_user_db, load_user_db

app = Flask(__name__)
users = load_user_db()
app.secret_key = 'secretkey'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jumpingsock.edubo@gmail.com'
app.config['MAIL_PASSWORD'] = 'mwougvaotdgcddti'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

class User:
    def __init__(self, id, uname, passw, email):
        self.id = id
        self.uname = uname
        self.passw = passw
        self.email = email

@app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    session.pop('user_id', None)

    if request.method == 'POST':

        uname = request.form['uname']
        passw = request.form['passw']

        try:
            user = [x for x in users if x.uname == uname][0]
        except:
            user = None
        else:
            if user and user.passw == passw:
                session['user_id'] = user.id
                return redirect(url_for('scratch_app'))
                
        login_error = "Nesprávné uživatelské jméno nebo heslo!"
        return render_template("index.html", login_error = login_error, uname = uname)
    
    return render_template("index.html")

@app.route('/scratch_app')
def scratch_app():
    if not g.user:
        return redirect(url_for('login'))
        
    return render_template("scratch-app.html")
    
@app.route('/registrace', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        reg_uname = request.form['reg_uname']
        reg_email = request.form['reg_email']
        reg_passw = request.form['reg_passw']

        if [x for x in users if x.uname == reg_uname]:
            reg_error = f'Uživatelské jméno "{reg_uname}" již existuje!'
            return render_template("registration.html", reg_error = reg_error)

        users.append(User(id=len(users) + 1, uname=reg_uname, passw=reg_passw, email=reg_email))
        update_user_db(users)
        return redirect(url_for('login'))
    
    return render_template("registration.html")
    
@app.route('/reset_passw', methods=['GET', 'POST'])
def reset_passw():
    if request.method == 'POST':

        reset_uname = request.form['reset_uname']
        reset_email = request.form['reset_email']

        try:
            user = [x for x in users if x.uname == reset_uname][0]
        except:
            reset_error = "Neznámé přihlašovací jméno!"
            return render_template("reset_passw.html", reset_error = reset_error)
        else:
            if user.email == reset_email:
                new_password = generate_random_password()
                users[users.index(user)].passw = new_password
                update_user_db(users)
                msg = Message('Obnovení Hesla', sender='jumpingsock.edubo@gmail.com', recipients=[reset_email])
                msg.body = f'Dobrý den {reset_uname},\nVaše nové heslo je:\n{new_password}\n\nWebová stránka Jumping Sock'
                mail.send(msg)
                return redirect(url_for('login'))
            else:
                reset_error = "Zadaný email nepatří k žádnému uživateli!"
                return render_template("reset_passw.html", reset_error = reset_error)
                
        reset_error = "Chyba při registraci, zkuste to prosím znovu"
        return render_template("reset_passw.html", reset_error = reset_error)

    return render_template("reset_passw.html")
