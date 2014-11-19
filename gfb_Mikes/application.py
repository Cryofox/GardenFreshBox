from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator

def main():
	session_factory = UnencryptedCookieSessionFactoryConfig('secretkey')
	config = Configurator(session_factory = session_factory)
	config.include('pyramid_chameleon')
	config.scan('views')
	return config.make_wsgi_app()
	
if __name__ == '__main__':
	app = main()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()
