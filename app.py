from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

# define the view using a function, which return a string
def hello_world():
    return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__":
    app.run()