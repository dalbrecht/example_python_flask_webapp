from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def welcome():  # put application's code here
    return render_template(
        'welcome.html',
        title="Example Start Page",
        description="This is an example start Page"
    )


@app.route('/details')
def details():
    return render_template(
        'details.html'
    )


@app.route('/autocomplete.json')
def autocomplete():
    return json.dumps([
        'red', 'blue', 'green', 'purple'
    ])


if __name__ == '__main__':
    app.run()
