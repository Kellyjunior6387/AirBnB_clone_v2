#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_session(exception=None):
    """Close the current sqlalchemy session"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Returns a html object with all state objects """
    states = storage.all("State")
    state_values = states.values()
    sorted_states = sorted(state_values, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)