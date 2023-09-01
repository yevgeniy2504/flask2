from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def about():
    return render_template('aboutus.html')


@app.route('/cont/')
def cont():
    return render_template('cont.html')


if __name__ == '__main__':
    app.run(debug=True)
