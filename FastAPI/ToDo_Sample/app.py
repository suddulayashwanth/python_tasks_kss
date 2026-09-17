from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main UI for the ToDo application."""
    return render_template('index.html')

if __name__ == '__main__':
    # Running presentation layer on port 5001 so it does not conflict with API
    app.run(port=5001, debug=True)
