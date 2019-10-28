from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


# @app.route('/greet')
# def greet():
#     return 'Hello'


# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return "Hello {}".format(name)


@app.route('/f/<celsius>')
def greet(celsius=""):
    return "{}".format(convert_celsius_to_fahrenheit(celsius))


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (int(fahrenheit) - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = int(celsius) * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
