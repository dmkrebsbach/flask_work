from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
## code below this line


# Level 1 - Three Blue Boxes
@app.route('/play')
def index():
    return render_template("playground.html", times=3)

# Level 2 - (X) Blue Boxes
@app.route('/play/<times>')
def index_play_num(times):
    return render_template("playground.html", times=int(times))	

# Level 3 - (X) (COLOR) Boxes
@app.route('/play/<times>/<color>')
def index_play_num_color(times, color):
    return render_template("playground.html", times=int(times),color=color)	

## code above this line    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.