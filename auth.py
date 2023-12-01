from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html",text="testing")

@auth.route('/logout')
def logout():
    return 'logout'

@auth.route('/sign_up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        if len(email) <4:
            flash('Email must be greter than 4 charcters.',category='error')

        elif len(firstname)<2:
            flash('First name  must be greter than 1 char',category='error')

        elif password1!=password2:
            flash('Password don\'t match',category='error')

        elif len(password1) <5:
            flash('Passord must be greter than 1 char',category='error')

        else:
            flash('Account created',category='success')
        
    return render_template("sign_up.html")