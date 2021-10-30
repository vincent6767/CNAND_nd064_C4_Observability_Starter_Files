from flask import Flask, render_template, request

from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

app = Flask(__name__)
metrics = GunicornInternalPrometheusMetrics(app)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/input-error')
def input_error():
    return "Record not found", 400

@app.route('/server-error')
def server_error():
    return "server error", 500

if __name__ == "__main__":
    app.run()