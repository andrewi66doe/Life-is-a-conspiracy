import flask, flask.views
import __mysql as database
class Login(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')
	def post(self):
		#logout if logout button pressed
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('index'))
		#required fields
		required = ['username', 'password']
		
		
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('index'))
		username = flask.request.form['username']
		password = flask.request.form['password']
		dbpassword = database.get_user_password(username)
		
		if dbpassword == password:
			flask.session['username'] = username
		else:
			flask.flash("Username doesn't exist or password is incorrect")
		return flask.redirect(flask.url_for('index'))
