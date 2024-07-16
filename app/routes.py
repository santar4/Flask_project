from flask_login import login_user, login_required
from flask import render_template, flash, redirect, url_for, request
from flask_wtf import form
from sqlalchemy import select
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.security import check_password_hash, generate_password_hash
from app import app, dB
from app.forms import LoginForm, SignUpForm, FeedbackForm
from app.models import Pizza, Feedback, User
from app.__init__ import name, schedule



@app.route('/')
def home():
    return render_template("base.html",
                           title="Crave Pizza Corner",
                           time_work=schedule,
                           name=name
                           )


@app.route('/menu/')
def menu_page():
    stmt = select(Pizza)
    pizzas = dB.session.execute(stmt).scalars()
    context = {
        "title": "Menu",
        "name": "Ordername",
        "time_work": schedule

    }
    return render_template("Menu.html", pizzas=pizzas, **context)


@app.route('/reviews/')
def feedback():
    stmt = select(Feedback)
    feedbacks = dB.session.execute(stmt).scalars()
    return render_template("Reviews.html", reviews=feedbacks, name=name)


@app.errorhandler(404)
def error_404(error):
    return render_template("Errors/404.html")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('Errors/500.html')


@app.route('/new_review/', methods=["GET", "POST"], endpoint='new_review')
@login_required
def feedbacks():
    form = FeedbackForm()
    if request.method == "POST":
        nickname = request.form.get("nickname")
        feedback = request.form.get("feedback")

        if not nickname:
            flash("Поле nickname необхідне для заповнювання")
        else:
            new_feedback = Feedback(
                nickname=nickname,
                feedback=feedback)
            dB.session.add(new_feedback)
            dB.session.commit()
            return redirect(url_for("home"))

    return render_template("New_review.html", form=form, name=name)




@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = dB.session.query(User).where(User.nickname == form.nickname.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("home"))
            flash("Wrong password")
            return redirect(url_for("login"))

        flash("Wrong nickname")
        return redirect(url_for("login"))

    return render_template("users/login_and_sign.up.html", form=form, title="Login", name=name)


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = dB.session.execute(dB.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("User currently exists")
            return redirect(url_for("login"))
        new_user = User(
            nickname=form.nickname.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        dB.session.add(new_user)
        dB.session.commit()
        return redirect(url_for("login"))
    return render_template("users/login_and_sign.up.html", form=form, title="Signup", name=name)
