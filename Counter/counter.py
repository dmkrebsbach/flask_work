
from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)
app.secret_key ="A random string of secretness"

@app.route("/")
def main():
    if "count" in session and "count_actual" in session:
        session["count"] += 1
        session["count_actual"] += 1
    else:
        session["count"] = 1
        session["count_actual"] = 1
    return render_template("counter.html", 
        countPlay = session["count"], 
        counterReal = session["count_actual"]
        )

@app.route("/destroy_session")
def sessionDestroyer():
    session["count"] = 0
    return redirect("/")            # use return redirect for all POST methods

@app.route("/add2")
def add2():
    session["count"] += 1
    return redirect("/")            # use return redirect for all POST methods

@app.route("/custom_increment", methods=["POST"])
def increment():
    session["count"] += (int(request.form["num"]) - 1)
    return redirect("/")            # use return redirect for all POST methods

if __name__ == "__main__":
    app.run(debug = True)