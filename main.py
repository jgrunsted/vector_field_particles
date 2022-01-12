from flask import Flask, request
from flask.templating import render_template
from flask import jsonify
import numpy as np
import particles

# commit testing

app = Flask(__name__)

particles = particles.Particles(np.array(["-x-y", "-y+x"]), 2000)

@app.route("/")
def draw():
    return render_template("particles.html", name=request.base_url)

@app.route("/_update_pos")
def update_positions():
    return jsonify(particles.update_particles())

if __name__ == "__main__":
    app.run()