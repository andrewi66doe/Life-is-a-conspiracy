import flask, flask.views

class Welcome(flask.views.MethodView):
	def get(self):
		return flask.render_template('home.html')
