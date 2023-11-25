from flask import Flask, render_template, g

import json

app = Flask(__name__)

@app.before_request
def before_request():
	with open("./db.json", "r") as file:
		g.db = json.load(file)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/solutions")
def solution_list():
	return render_template("solutions.html")

@app.route("/trial/<trial>")
def solution_trial(trial):
	
	# getting a trial solution data from database
	solutions     = g.db["solutions"]
	current_trial = solutions["trial"][trial]
	title         = current_trial["title"]
	description   = current_trial["description"]
	author        = current_trial["author"]
	input_format  = current_trial["input-format"]
	output_format = current_trial["output-format"]
	example_io    = current_trial["example-io"]
	solution      = current_trial["solution"]
	efficiency    = current_trial["efficiency"]
	complexity    = current_trial["complexity"]
	explanation   = current_trial["explanation"]

	return render_template("./trial/trial.html",
			title=title,
			description=description,
			author=author,
			input_format=input_format,
			output_format=output_format,
			example_io=example_io,
			solution=solution,
			efficiency_type=efficiency[0],
			efficiency=efficiency[1],
			complexity=complexity,
			explanation=explanation,
			enumerate=enumerate,
	)

if __name__ == "__main__":
	app.run(debug=True)