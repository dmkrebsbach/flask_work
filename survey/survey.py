from flask import Flask, render_template, request
app = Flask(__name__)
## Code Below This Line ##

@app.route("/")
def mainRoute():
    return render_template("survey.html")

@app.route("/display", methods=["POST"])        ## ensure to include methods statement within app.route
def display():
    name = request.form["name"]                 ## for all of the input portions, ensure the 'name' of each element matches the python sheet
    dojo = request.form["dojo"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template("results.html",      ## make sure the return render_template goes to the right .html file!
        name = name,
        dojo = dojo,
        language = language,
        comment = comment
    )

## Code Above This Line
if __name__ == "__main__":
    app.run(debug = True)