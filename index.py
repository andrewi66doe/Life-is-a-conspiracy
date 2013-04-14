import flask
import settings
import __mysql as database
from wsgiref.handlers import CGIHandler
from main import *
app = flask.Flask(__name__)
app.secret_key = settings.secret_key


app.add_url_rule('/tables/',
	    view_func=Tables.as_view('tables'),
	    methods=['GET','POST'])
app.add_url_rule('/login/',
		view_func=Login.as_view('index'),
		methods=['GET','POST'])
app.add_url_rule('/',
		view_func=Welcome.as_view('welcome'),
		methods=['GET'])
app.add_url_rule('/remote/',
		view_func=Remote.as_view('remote'),
		methods=['GET','POST'])
app.add_url_rule('/music/',
		view_func=Music.as_view('music'),
		methods=['GET'])
app.add_url_rule('/posts/',
		view_func=Posts.as_view('posts'),
		methods=['GET','POST'])
@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'),404
app.debug = True
app.run(host="0.0.0.0")
#CGIHandler().run(app)

