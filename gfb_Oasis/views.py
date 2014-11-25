from pyramid.renderers import get_renderer
from pyramid.view import view_config
from controller import (
	process_login_request,
	process_logout_request
)
from GFBDatabaseController import GFBDatabaseController
import json
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
#Used to Update DB







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


########## INBETWEENS



#Helper function to parse through Fields, returns list
def ParseFields(ajaxSTR):
	paramList = str(ajaxSTR.params).split("&")
	#for i in range (len(paramList)):
		#Strip off fieldX= from strings
	#	paramList[i] =  (paramList[i].split("="))[1]

	return paramList