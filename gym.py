from flask import Flask, render_template
import os

from controllers.member_controller import members_blueprint
from controllers.instructor_controller import instructors_blueprint
from controllers.activity_controller import activities_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(instructors_blueprint)
app.register_blueprint(activities_blueprint)


@app.route("/")
def home():
    return render_template("index.html", title="Home")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)