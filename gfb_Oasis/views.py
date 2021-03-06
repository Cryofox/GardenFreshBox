from pyramid.renderers import get_renderer
from pyramid.view import view_config
from controller import (
	process_login_request,
	process_logout_request
)
from GFBDatabaseController import GFBDatabaseController
import json


'''
	returns the unchanging layout of the site that will be on every page.
'''
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


'''
	get the webpage for a user who is logging into the system
'''
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


'''
	a template for Foundation, the webpage builder we are using 
'''
			#    V Template Location                                V Argument 
@view_config(renderer="templates/FoundationTemplate.pt",name="FoundationTemplate")
def Foundation_view(request):
	return {"layout": site_layout(), "user_header": user_header(request), "location": "FoundationTemplate"}

'''
	get the webpage for signing up to the site
'''
@view_config(renderer="templates/signup.pt", name="signup")
def signup_view(request):
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Sign Up"}
																			## Match Header? ^



'''
	get the webpage when logging out of the system.
'''
@view_config(name="logout")
def logout_view(request):
	return process_logout_request(request)




#############
# OASIS_GFB PAGES
#############
'''
	get the specific header for the person logged in
'''
@view_config(renderer="templates/GardenFreshBox_Home.pt")
def index_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "GardenFreshBox_Home"}
	#return 'Ok'
@view_config(renderer='json', xhr=True )
def index_ajax(request):	
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))

'''
	get the webpage where the user can order product
'''
@view_config(renderer="templates/BuyGoodies.pt",name="BuyGoodies")
def BuyGoodies_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Buy Goodies"}
	#return 'Ok'
@view_config(renderer='json',name="BuyGoodies", xhr=True )
def BuyGoodies_ajax(request):
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))	

'''
	get the webpage that displays the newsletters by GFB
'''
@view_config(renderer="templates/News.pt",name="News")
def News_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "News"}
	#return 'Ok'
@view_config(renderer='json',name="News", xhr=True )
def News_ajax(request):
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))	

'''
	get the webpage that displays the locations of the host sites
'''
@view_config(renderer="templates/PickupLocations.pt",name="PickupLocations")
def PickupLocations_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "PickupLocations"}
	#return 'Ok'
@view_config(renderer='json',name="PickupLocations", xhr=True )
def PickupLocations_ajax(request):
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))	

'''
	get the webpage that displays orders for admins specifically
'''
@view_config(renderer="templates/Admin_Sales.pt",name="Admin_Sales")
def Admin_Sales_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Admin_Sales"}
	#return 'Ok'

#Atm Dates Are HardCoded, if time permits, I'll figure out a way to pass date values in
@view_config(renderer='json',name="Admin_Sales", xhr=True )
def Sales_ajax(request):

	print "Params="+request.params["field1"]

	if (request.params["field1"]=="Fetch"):
		#test = "hello"
		myDB = GFBDatabaseController();
		records=myDB.getAllOrdersByDistributionDate("1900-01-30","3000-01-30")

		recordList= list()
		for x in range(len(records)):
			valList = list()
			for y in range(len(records[x])):
				valList.append( str(records[x][y]));

			recordList.append(valList);

		print "Records="+str(records)
		print "JSON DUMP="+json.dumps(recordList)
	    #return records
		return (json.dumps(recordList))

	if (request.params["field1"]=="UpdateOrder"):
		myDB = GFBDatabaseController();
		#Update Order
		myDB.updateOrder(
			request.params["field2"], 
			request.params["field9"],
			request.params["field9"],
			request.params["field3"],
			request.params["field4"],
			request.params["field6"],
			request.params["field5"],
			0,
			request.params["field8"],
			request.params["field7"],
			request.params["field12"],
			request.params["field11"],
			request.params["field13"],
			request.params["field13"],
			"Dynamic!");
		return 

	if (request.params["field1"]=="AddNewOrder"):
		myDB = GFBDatabaseController();
		#Update Order
		myDB.createNewOrder(
			request.params["field9"],
			request.params["field9"],
			request.params["field3"],
			request.params["field4"],
			request.params["field6"],
			request.params["field5"],
			False,
			request.params["field8"],
			request.params["field7"],
			request.params["field12"],
			0,
			None,
			request.params["field11"],
			request.params["field13"],
			request.params["field13"],
			"Dynamic!");
		return 		
	if (request.params["field1"]=="DeleteOrder"):
		myDB = GFBDatabaseController();
		#Update Order
		myDB.removeOrder(
			request.params["field2"]);
		return 	
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))

#Used to Update DB






'''
	get the webpage that displays the information of the host sites for admins specifically
'''
@view_config(renderer="templates/Admin_HostSites.pt",name="Admin_HostSites")
def HostSite_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Admin_HostSites"}
	#return 'Ok'
#Atm Dates Are HardCoded, if time permits, I'll figure out a way to pass date values in
#Atm Dates Are HardCoded, if time permits, I'll figure out a way to pass date values in
@view_config(renderer='json',name="Admin_HostSites", xhr=True )
def HostSite_ajax(request):

	print "Params="+request.params["field1"]

	if (request.params["field1"]=="Fetch"):
		#test = "hello"
		myDB = GFBDatabaseController();
		records=myDB.getAllHostSites()

		recordList= list()
		for x in range(len(records)):
			valList = list()
			for y in range(len(records[x])):
				valList.append( str(records[x][y]));

			recordList.append(valList);

		print "Records="+str(records)
		print "JSON DUMP="+json.dumps(recordList)
	    #return records
		return (json.dumps(recordList))

	if (request.params["field1"]=="UpdateHostSite"):
		myDB = GFBDatabaseController();
		#Update Order
		myDB.updateHostSite(
			request.params["field2"], 
			request.params["field3"],
			request.params["field4"],
			request.params["field5"],
			request.params["field6"],
			request.params["field7"],
			request.params["field8"],
			request.params["field9"]
			);
		return 

	if (request.params["field1"]=="AddNewHostSite"):
		print ("ADD NEW IS CALLED")
		myDB = GFBDatabaseController();
		#Update Order
		myDB.addHostSite(
			request.params["field2"], 
			request.params["field3"],
			request.params["field4"],
			request.params["field5"],
			request.params["field6"],
			request.params["field7"],
			request.params["field8"]
			);
		return 		
	if (request.params["field1"]=="DeleteHostSite"):
		myDB = GFBDatabaseController();
		#Update Order
		myDB.removeHostSite(
			request.params["field2"]);
		return 	
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))

'''
	get the webpage the user is sent to when they are logged in, the admin dashboard
'''
@view_config(renderer="templates/Admin_Users.pt",name="Admin_Users")
def User_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Admin_Users"}
	#return 'Ok'
#Atm Dates Are HardCoded, if time permits, I'll figure out a way to pass date values in
@view_config(renderer='json',name="Admin_Users", xhr=True )
def User_ajax(request):
	if (request.params["field1"]=="Fetch"):
		#test = "hello"
		myDB = GFBDatabaseController();
		records=myDB.getUsers()

		recordList= list()
		for x in range(len(records)):
			valList = list()
			for y in range(len(records[x])):
				valList.append( str(records[x][y]));

			recordList.append(valList);

		print "Records="+str(records)
		print "JSON DUMP="+json.dumps(recordList)
	    #return records
		return (json.dumps(recordList))

	if (request.params["field1"]=="AddNewUser"):
		print ("ADD NEW IS CALLED")
		myDB = GFBDatabaseController();
		#Update Order
		myDB.addUser(
			request.params["field2"], 
			request.params["field3"],
			request.params["field4"],
			request.params["field5"],
			request.params["field6"],

			None,
			request.params["field7"]
			);
		return 		
	if (request.params["field1"]=="DeleteUser"):
		myDB = GFBDatabaseController();
		#Update Order
		myDB.removeUser(
			request.params["field2"]);
		return 
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))

'''
	get the webpage that displays the FAQ of GFB
'''
@view_config(renderer="templates/FAQ.pt",name="FAQ")
def FAQ_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "FAQ"}
	#return 'Ok'
@view_config(renderer='json',name="FAQ", xhr=True )	
def FAQ_ajax(request):
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))	

'''
	get the webpage that displays the recipies given by GFB
'''
@view_config(renderer="templates/Recipes.pt",name="Recipes")
def Recipes_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "Recipes"}
	#return 'Ok'	

@view_config(renderer='json',name="Recipes", xhr=True )	
def Recipes_ajax(request):
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))	


'''
	get the webpage that displays the contact info of GFB 
'''
@view_config(renderer="templates/ContactUs.pt",name="ContactUs")
def ContactUS_view(request):
	#if the user is logged in redirect to the appropriate home page
	return {"layout": site_layout(), "user_header": user_header(request), "location": "ContactUs"}
	#return 'Ok'		

@view_config(renderer='json',name="ContactUs", xhr=True )
def ContactUS_ajax(request):
	if (request.params["field1"]=="Login"):
		#test = "hello"
		myDB = GFBDatabaseController();

		return (json.dumps(myDB.getLogin(request.params["field2"],request.params["field3"]) ))	


########## INBETWEENS


'''
	helper function to parse through Fields, returns list
'''
def ParseFields(ajaxSTR):
	paramList = str(ajaxSTR.params).split("&")
	#for i in range (len(paramList)):
		#Strip off fieldX= from strings
	#	paramList[i] =  (paramList[i].split("="))[1]

	return paramList
