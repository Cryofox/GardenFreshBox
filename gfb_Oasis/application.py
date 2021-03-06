from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator

def main():
	session_factory = UnencryptedCookieSessionFactoryConfig('secretkey')
	config = Configurator(session_factory = session_factory)
	config.include('pyramid_chameleon')
	config.scan('views')
	#config.add_route('FoundationTemplate', '/FoundationTemplate')
	config.add_static_view('static', 'static/', cache_max_age=86400)
	return config.make_wsgi_app()
	

if __name__ == '__main__':
	app = main()
	print("main-wow");
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()

