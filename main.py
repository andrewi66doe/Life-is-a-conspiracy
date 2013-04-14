import flask, flask.views
import __mysql as database
import os
import utils



class Tables(flask.views.MethodView):
	@utils.login_required
	def get(self):
		data = database.read_table_data()
		profit = float( data[0][2]) - float(data[0][1])
		return flask.render_template('tables.html',data = data, profit = profit)
	@utils.login_required
	def post(self):
		pass		
class Welcome(flask.views.MethodView):
	def get(self):
		return flask.render_template('home.html')


class Remote(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template("remote.html")
	@utils.login_required
	def post(self):
		
		#result = eval( flask.request.form['expression'])
		flask.flash("The interpreter is currently disabled")
		return flask.render_template("remote.html")
		
class Posts(flask.views.MethodView):
	@utils.login_required
	def get(self):
		posts = database.get_posts()
		return flask.render_template('posts.html', posts=posts)
	@utils.login_required
	def post(self):
                #required fields
                required = ['postname', 'post']
                post = flask.request.form['post']
		postname = flask.request.form['postname']
		username = flask.session['username']
		#if posting field is not empty
                if postname and post!='\t\r\n\t':
			database.post_to_database(username,post,postname)
			return flask.redirect(flask.url_for('posts'))
                else:
			flask.flash("please fill out all fields")
                	return flask.redirect(flask.url_for('posts'))
                #flask.flash(username)
                
class Music(flask.views.MethodView):
	@utils.login_required
	def get(self):
		songs = os.listdir("static/music")
		return flask.render_template('music.html', songs=songs)
		
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
