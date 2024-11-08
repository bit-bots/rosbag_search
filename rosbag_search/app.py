from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def rosbag_search():
    return render_template('rosbag_search.html')

@app.route("/<name>")
def hello_lea(name=None):
    return render_template('test.html', person=name)

@app.route("/bag")
def show_bag():
    return render_template('bag.html')


if __name__ == '__main__': app.run()