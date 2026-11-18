
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    try:
        members = int(request.form["members"])

        activities = [
            "bathing",
            "cooking",
            "washing",
            "cleaning",
            "gardening",
            "other"
        ]

        values = {}

        for activity in activities:
            value = float(request.form[activity])

            if value < 0:
                raise ValueError

            values[activity] = value

        if members <= 0:
            raise ValueError

        total = sum(values.values())
        per_person = total / members

        return render_template(
            "index.html",
            total=total,
            per_person=per_person,
            values=values
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            error="Please enter valid positive numbers."
        )


if __name__ == "__main__":
    app.run(debug=True)
