import flask, flask.views
import os
import utils
import  __mysql as mysql

class Posts(flask.views.MethodView):
	@utils.login_required
	def get(self):
		posts = mysql.get_posts()
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
			mysql.post_to_database(username,post,postname)
			return flask.redirect(flask.url_for('posts'))
                else:
			flask.flash("please fill out all fields")
                	return flask.redirect(flask.url_for('posts'))
                #flask.flash(username)
		
