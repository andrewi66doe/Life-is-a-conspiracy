import flask
import _mysql as mysql
import datetime
import settings


#BEGIN mysql functions for authentication
def get_user_password(username):
	userdb =  mysql.connect(settings.DATABASE_LOCATION,
							settings.USERNAME,
							settings.PASSWORD,
							settings.USER_DATABASE)
	userdb.query("SELECT password FROM users WHERE username='%s'" % username.strip("'"))
	result = userdb.store_result().fetch_row()#retrieving password as a two dimensional tuple
	if result:
		password = result[0][0] #fetching password from a tuple that is retrieved from the data base
		return password
	userdb.close()

#BEGIN mysql functions for posts
def get_posts():
	postdb = mysql.connect(settings.DATABASE_LOCATION,
							settings.USERNAME,
							settings.PASSWORD,
							settings.POST_DATABASE)
	postdb.query("SELECT * FROM posts")
	r = postdb.store_result()
	data = reversed(r.fetch_row(maxrows=0))
	return data
	postdb.close()
"""def get_post_by_id(id):
	postdb = mysql.connect(settings.DATABASE_LOCATION,'settings.USERNAME','settings.PASSWORD',settings.POST_DATABASE)
	postdb.query("SELECT * FROM posts WHERE id=%i" % id)
    r = postdb.store_result()
    data = r.fetch_row()
    return data[0]
	postdb.close()"""

def number_of_posts():
	postdb = mysql.connect(settings.DATABASE_LOCATION,
							settings.USERNAME,
							settings.PASSWORD,
							settings.POST_DATABASE)
	postdb.query("SELECT id FROM posts")
	posts = len( postdb.store_result().fetch_row(maxrows=0))#maxrows = 0 retrieves all rows as opposed to just one
	return posts
	postdb.close()
		
	

def post_to_database(username,content,name):
	postdb = mysql.connect(settings.DATABASE_LOCATION,
						   settings.USERNAME,
						   settings.PASSWORD,
						   settings.POST_DATABASE)
	date = datetime.date.today().strftime("%B %d, %Y")
	postdb.query("INSERT INTO posts (username,date,post,postname) VALUES('%s','%s','%s','%s')" % (username,date,content,name))
	postdb.close()

def clear_all_posts(username):
	postdb.query("DELETE FROM posts WHERE username='%s'") % username
	postdb.close()
def read_table_data():
	tabledb = mysql.connect(settings.DATABASE_LOCATION,
						   settings.USERNAME,
						   settings.PASSWORD,
						   settings.TABLE_DATA)
	tabledb.query("select * from data")
	tb = tabledb.store_result().fetch_row(maxrows=0)
	return tb
	tabledb.close()


