from flask import Blueprint,render_template
views=Blueprint('views',__name__)
#here the above Blueprint is used for routing page foe views


@views.route('/')
def home():
    return render_template("home.html")