from os import environ as env
import flask

app = flask.Flask(__name__)

secret_ip = env["IP"]

@app.route("/")
def index():
	return flask.render_template("index.html"), 200

@app.route("/auth")
def auth():
	ip_address = flask.request.remote_addr
	if ip_address == secret_ip:
		return flask.render_template("success.html"), 200
	else:
		return "403 Unauthorized", 403

app.run(host="0.0.0.0", port=8080)