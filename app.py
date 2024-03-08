from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'R 70 000,00'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'SA, Remote',
    'salary': 'R 120000,00'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'SA, Johannesburg',
    'salary': 'R 80 000,00'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'SA, Remote',
    'salary': 'R 85 000,00'
}]


@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)
