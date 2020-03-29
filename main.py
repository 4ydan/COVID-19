from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def format_time():
    t = datetime.datetime.now()
    s = t.strftime('%Y-%m-%d %H:%M:%S.%f')
    return s[:-10]


posts = [
    {
    },
]


@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home():
    return render_template('home.html',)


@app.route("/forecast")
def forecast():
    from data import MyClass
    bar = MyClass().to_json()
    return render_template('forecast.html', posts=posts,  plot=bar)


if __name__ == '__main__':
    app.run(debug=True)
