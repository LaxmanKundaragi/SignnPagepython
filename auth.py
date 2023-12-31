from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
auth=Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()

        if user:
            # if check_password_hash(user.password,password):
            if(user.password,password):
                flash('Logged in Succesfully',category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Passord',category='error')
        else:
            flash('Email does not exist',category='error')         
    return render_template("login.html",boolean=True)

@auth.route('/logout')
def logout():
    return redirect(url_for(auth.login))

@auth.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        user=User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists',category='error')

        elif len(email) <4:
            flash('Email must be greter than 4 charcters.',category='error')

        elif len(firstname)<2:
            flash('First name  must be greter than 1 char',category='error')

        elif password1!=password2:
            flash('Password don\'t match',category='error')

        elif len(password1) <5:
            flash('Passord must be greter than 1 char',category='error')

        else:
            new_user=User(email=email,first_name=firstname,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created',category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")