from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')    
    return "This is my updated flask application"

if __name__ == "__main__":
    app.run() 
    # requirement.txt sari lib ko contain krti hai ik jagah