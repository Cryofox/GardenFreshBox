from pyramid.renderers import get_renderer
from pyramid.view import view_config
from controller import (
	process_login_request,
	process_logout_request
)

def site_layout():
	renderer = get_renderer("templates/core_layout.pt")
	return renderer.implementation().macros['layout']

'''
get the specific header for the person logged in
'''
def user_header(request):
	if not 'username' in request.session:
		with open('templates/user_header.pt') as f:
			return f.read()
	else:
		with open('templates/admin_header.pt') as f:
			return f.read()



@view_config(renderer="templates/login.pt", name="login")
def login_view(request):
	if 'username' in request.params: #there's gotta be a better way to do page permissions
		return HTTPFound("/")
	if 'login.submit' in request.params and request.params['login.submit'] == 'login':
		return process_login_request(request)
	ret = {"layout": site_layout(), "user_header": user_header(request), "location": "Log In"}
	if 'error' in request.params: #if there was a login error give a meaningful message
		if request.params['error'] == '1':
			ret['error1'] = True
		elif request.params['error'] == '2':
			ret['error2'] = True
	return ret



			#    V Template Location                                V Argument 
@view_config(renderer="templates/FoundationTemplate.pt",name="FoundationTemplate")
def Foundation_view(request):
	return {"layout": site_layout(), "user_header": user_header(request), "location": "FoundationTemplate"}

@view_config(renderer="templates/signup.pt", name="signup")
def signup_view(request):
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Sign Up"}
																			## Match Header? ^




@view_config(name="logout")
def logout_view(request):
	return process_logout_request(request)




############## OASIS_GFB PAGES
@view_config(renderer="templates/GardenFreshBox_Home.pt")
def index_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Home"}
	#return 'Ok'

@view_config(renderer="templates/BuyGoodies.pt",name="BuyGoodies")
def BuyGoodies_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Buy Goodies"}
	#return 'Ok'
@view_config(renderer="templates/News.pt",name="News")
def News_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "News"}
	#return 'Ok'
@view_config(renderer="templates/PickupLocations.pt",name="PickupLocations")
def PickupLocations_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "PickupLocations"}
	#return 'Ok'


@view_config(renderer="templates/Admin_Sales.pt",name="Admin_Sales")
def Admin_Sales_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Admin_Sales"}
	#return 'Ok'

@view_config(renderer='json',name="Admin_Sales", xhr=True )
def ajax(request):
    test = "hello"
    return dict(test=test)

########## INBETWEENS


