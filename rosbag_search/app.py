from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def rosbag_search():
    return render_template('rosbag_search.html')

@app.route("/<name>")
def hello_lea(name=None):
    return render_template('test.html', person=name)

if __name__ == '__main__': app.run()