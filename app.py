from flask import Flask, render_template, request, session, flash, redirect, url_for
from website.database import load, save

app = Flask(__name__)
app.secret_key = "your_secret_key"


# Homepage route
@app.route("/")
def home():
    return render_template("main.html")


# About route
@app.route("/about")
def about():
    return render_template("about.html")


# Skills route
@app.route("/skills")
def skills():
    return render_template("skills.html")


# Contact route
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    data = load()
    if request.method == "POST":
        firstname = (request.form.get("user_firstname") or "").title().strip()
        surname = (request.form.get("user_surname") or "").title().strip()
        email = request.form.get("user_email").lower().strip()
        password = request.form.get("user_password")
        confirm_password = request.form.get("confirm_user_password")
        selected_course = request.form.get("course")

        # Checking for any empty entry
        if (
            not firstname
            or not surname
            or not email
            or not password
            or not confirm_password
        ):
            flash("Warning: All fields are required!")
            return redirect(url_for("register"))

        # Checking user doesn't select default cause
        if selected_course == "default":
            flash("Can not select default course. Select one from the dropdown")
            return redirect(url_for("register"))

        # Checking if user email already exist
        if email in data:
            flash("User already exists!. Log in here")
            return redirect(url_for("login"))

        # Checking if password matches
        if password != confirm_password:
            return "Passwords do not match!"
        else:
            data[email] = {
                "email": email,
                "firstname": firstname,
                "surname": surname,
                "password": password,
                "course": selected_course,
            }
            save(data)

        # Directing users to their choosing couse
        session["email"] = email  # log the user in
        if selected_course == "sonography":
            return redirect(url_for("sonography"))
        elif selected_course == "programming":
            return redirect(url_for("programming"))
        else:
            return redirect(url_for("design"))
    return render_template("register.html")


# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = load()
        email = request.form.get("email").lower()
        password = request.form.get("password")
        if email in data:
            stored_password = data[email].get("password")

        if not stored_password:
            flash("User data corrupted. Please register again.")
            return redirect(url_for("register"))

        if password == stored_password:
            session["email"] = email
            if data[email].get("course") == "sonography":
                return render_template("scan/sonography.html")
            elif data[email].get("course") == "programming":
                return render_template("development/programming.html")
            else:
                return render_template("graphic_design/design.html")
        else:
            flash("Incorrect password or email.")
            return redirect(url_for("login"))
    return render_template("login.html")


# Use this in the user profile
# User changing password route
@app.route("/reset", methods=["GET", "POST"])
def reset():
    data = load()

    email = session.get("email")

    if not email:
        flash("Please login first")
        return redirect(url_for("login"))

    user = data.get(email)

    if request.method == "POST":
        old_password = request.form.get("old_user_password")
        new_password = request.form.get("new_user_password")
        confirm_new_password = request.form.get("confirm_new_user_password")

        if old_password != user["password"]:
            flash("Old password is incorrect")
            return redirect(url_for("reset"))

        if new_password != confirm_new_password:
            flash("New passwords do not match")
            return redirect(url_for("reset"))

        user["password"] = new_password
        save(data)

        flash("Password changed successfully")
        return redirect(url_for("profile"))

    return render_template("change_password.html", email=email)


# Forgot password route
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    data = load()
    if request.method == "POST":
        email = request.form.get("user_email")
        old_password = request.form.get("old_user_password")
        new_password = request.form.get("new_user_password")
        confirm_new_password = request.form.get("confirm_new_user_password")
        # Validate inputs
        if not all([email, old_password, new_password, confirm_new_password]):
            flash("Warning: All fields are required")
            return redirect(url_for("forgot_password"))
        # Normalize
        email = email.lower().strip()
        old_password = old_password.lower().strip()
        new_password = new_password.lower().strip()
        confirm_new_password = confirm_new_password.lower().strip()
        # Check user exists
        if email not in data:
            flash("No such user found. Register here")
            return redirect(url_for("register"))
        # Check old password
        if data[email]["password"] != old_password:
            flash("Old password is incorrect")
            return redirect(url_for("forgot_password"))
        # Check new passwords match
        if new_password != confirm_new_password:
            flash("New password mismatched")
            return redirect(url_for("forgot_password"))
        # Save new password
        data[email]["password"] = new_password
        save(data)
        flash("Password changed successfully")
        return redirect(url_for("login"))
    return render_template("forgot_password.html")


# Ultrasound physics route
@app.route("/ultrasound")
def ultrasound():
    return render_template("scan/ultrasound.html")


# Dopper physics route
@app.route("/doppler")
def doppler():
    return render_template("scan/doppler.html")


# Gynecology route
@app.route("/gynecology")
def gynecology():
    return render_template("scan/gynecology.html")


# Obstetrics route
@app.route("/obstetrics")
def obstetrics():
    return render_template("scan/obstetrics.html")


# Abdominal route
@app.route("/abdominal")
def abdominal():
    return render_template("scan/abdominal.html")


# Musculoskeletal route
@app.route("/musculoskeletal")
def musculoskeletal():
    return render_template("scan/musculoskeletal.html")


# Small parts route
@app.route("/smallparts")
def smallparts():
    return render_template("scan/smallparts.html")


# Umbilical artery doppler route
@app.route("/umbilical")
def umbilical():
    return render_template("scan/umbilical.html")


# Uterine artery doppler route
@app.route("/uterine")
def uterine():
    return render_template("scan/uterine.html")


# Venous doppler route
@app.route("/venous")
def venous():
    return render_template("scan/venous.html")


# Waveforms interpretation route
@app.route("/waveforms")
def waveforms():
    return render_template("scan/waveforms.html")


# Middle cerebral artery doppler route
@app.route("/middle_c")
def middle_c():
    return render_template("scan/middle_c.html")


# Ductus venosus route
@app.route("/ductus")
def ductus():
    return render_template("scan/ductus.html")


# Cerebroplacental ratio doppler route
@app.route("/cerebro")
def cerebro():
    return render_template("scan/cerebro.html")


# Aterial doppler route
@app.route("/arterial")
def arterial():
    return render_template("scan/arterial.html")


# DVT route
@app.route("/dvt")
def dvt():
    return render_template("scan/dvt.html")


# Programming home page route
@app.route("/programming")
def programming():
    return render_template("development/programming.html")


# Python route
@app.route("/python")
def python():
    return render_template("development/python.html")


# CSS route
@app.route("/cascading")
def cascading():
    return render_template("development/cascading.html")


# HTML route
@app.route("/html_page")
def html_page():
    return render_template("development/html_page.html")


# Javascript route
@app.route("/javascript")
def javascript():
    return render_template("development/javascript.html")


# React route
@app.route("/react")
def react():
    return render_template("development/react.html")


# Nodejs route
@app.route("/nodejs")
def nodejs():
    return render_template("development/nodejs.html")


# Flask route
@app.route("/flasks")
def flasks():
    return render_template("development/flasks.html")


# Express route
@app.route("/express")
def express():
    return render_template("development/express.html")


# Graphic desing home page route
@app.route("/design")
def design():
    return render_template("graphic_design/design.html")


# Graphic design fundamentals
@app.route("/fundamentals")
def fundamentals():
    return render_template("graphic_design/fundamentals.html")


# Typography route
@app.route("/typography")
def typography():
    return render_template("graphic_design/typography.html")


# Color route
@app.route("/color")
def color():
    return render_template("graphic_design/color.html")


# Software route
@app.route("/software")
def software():
    return render_template("graphic_design/software.html")


# Logo route
@app.route("/logo")
def logo():
    return render_template("graphic_design/logo.html")


# uiux route
@app.route("/uiux")
def uiux():
    return render_template("graphic_design/uiux.html")


# projects route
@app.route("/projects")
def projects():
    return render_template("graphic_design/projects.html")


# photoshop route
@app.route("/photoshop")
def photoshop():
    return render_template("graphic_design/photoshop.html")


# aftereffects route
@app.route("/aftereffects")
def aftereffects():
    return render_template("graphic_design/aftereffects.html")


# illustrator route
@app.route("/illustrator")
def illustrator():
    return render_template("graphic_design/illustrator.html")


# coreldraw route
@app.route("/coreldraw")
def coreldraw():
    return render_template("graphic_design/coreldraw.html")


# figma route
@app.route("/figma")
def figma():
    return render_template("graphic_design/figma.html")


# canva route
@app.route("/canva")
def canva():
    return render_template("graphic_design/canva.html")


# Courses route
@app.route("/courses")
def courses():
    return render_template("courses.html")


if __name__ == "__main__":
    app.run(debug=True)
