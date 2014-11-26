from pyramid.httpexceptions import HTTPFound
import hashlib
import GFBDatabaseController

'''
	logs the user into the system with the given request, containg a username and password
'''
def process_login_request(request):
	if not 'user' in request.params or not 'pass' in request.params or request.params['user'] == '' or request.params['pass'] == '':
		return HTTPFound(location='login?error=1')
	username = request.params['user']
	password = hashlib.sha224(request.params['pass'].encode('utf-8')).hexdigest()
	with open('auth/users.auth') as f:
		for line in f.readlines():
			auth = line.split(';')
			if username.strip() == auth[0].strip() and password.strip() == auth[1].strip():
				request.session['username'] = username
				return HTTPFound(location="/")
	return HTTPFound(location="login?error=2")


	'''
		logs the user out of the system with the given request, containg a username
	'''
def process_logout_request(request):
	del request.session['username']
	return HTTPFound("/")


	'''
		updates the users record with the given request, containing a username
	'''
def process_UpdateRecord_request(request):
	del request.session['username']
	return
	#return HTTPFound("/")


