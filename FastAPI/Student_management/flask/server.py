from app import app

if __name__ == '__main__':
    print("Launching Student Management Portal on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
