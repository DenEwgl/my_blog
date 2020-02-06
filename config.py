class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/test1'
	SECRET_KEY = 'nice secret'