#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
from array import array

class GFBDatabaseController:
#Credentials: 1= Admin, 2 = Coordinator

	#############
	#User Functions
	#############
	'''
		Check if an email is already used by a user in the database.
	'''
	def userExists(self, email_str):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#Check if HostSite Exists
			## Add HostSite to Table
			cur.execute("SELECT email FROM TBL_USERS WHERE email=\'"+email_str+"\'");
			records=cur.fetchall()

			if(len(records)>0):
				return True

		return False


	'''
		Adds a new user to the database.
		This is used by administrators to create new user accounts 
		for host site coordinators and for other administrators
  	'''
	def addUser(self, email_str,pass_str, fName_str, lName_str, phoneNum_str, hstSite_iArr, credentials_i):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:

			cur = con.cursor()
			if(not self.userExists(email_str)):
				##Check if HostSites in our List exist
				#If a "non empty" HostSite list was passed
				if(hstSite_iArr is not None):
					for x in range (len(hstSite_iArr)):
						# If the Host Site Does not exist in the DB return false
						if ( self.getHostSite(hstSite_iArr[x]) == None ):
							print "Add User FAILED: A Link was attempted with a non-existing Host Site"
							return False


				## Add User to Table
				cur.execute("INSERT INTO TBL_USERS VALUES (null,\'"+email_str+"\',\'"+pass_str+"\',\'"+fName_str+"\',\'"+lName_str+"\',\'"+phoneNum_str+"\',"+str(credentials_i)+")");

				#Grab Added User ID
				cur.execute("SELECT * FROM TBL_USERS WHERE email=\'"+email_str+"\'");
				record=cur.fetchall()
				print str(record[0][0])
				
				## Update Hostsite(s) Rel with this User
				if(hstSite_iArr is not None and record>0):
					for x in range (len(hstSite_iArr)):			
						cur.execute("INSERT INTO TBL_COORDINATOR_HOSTSITE_REL VALUES (null,"+str(record[0][0])+","+str(hstSite_iArr[x])+")");
				print "Success!"

				return True
		print "ADDING USER:FAILED"
		return False


	'''
 		Authenticate the users account
 		Check if the given password for a user matches what's in 
  *  	the database for them
  	'''
	def authUser(self, email_str,pass_str, fName_str, lName_str, phoneNum_str, hstSite_iArr, credentials_i):
		return true

	'''
		updates the user profile with the given information.
	'''
	def updateUser(self, email_str, newEmail_str,newPassword_str, newFirstName_str,newLastName_str, newPhoneNumber_str, hostSites_iAr,credentials_i):
 		return true

	'''
		returns the records of all users in the system
	'''
 	def getUsers(self):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		with con: 

			cur = con.cursor()

			##Check if HostSites in our List exist
			cur.execute("SELECT * FROM TBL_USERS");

			records = cur.fetchall()
			if(len(records)>0):
				return records

		return None	


	'''
		returns the records of a specific user in the system identified by their email as a string
	'''
 	def getUser(self, email_str):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		with con:

			cur = con.cursor()

			##Check if HostSites in our List exist
			cur.execute("SELECT * FROM TBL_USERS WHERE email="+str(email_str));

			Dict = cur.fetchall()
			if(len(Dict)>0):
				#Return the first Row (The Only Row)
				return Dict

		return None

	'''
		returns the records of a specific user in the system identified by their userid
	'''
 	def getUser(self, userid):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		with con:

			cur = con.cursor()

			##Check if HostSites in our List exist
			cur.execute("SELECT * FROM TBL_USERS WHERE id="+str(userid));

			Dict = cur.fetchall()
			if(len(Dict)>0):
				#Return the first Row (The Only Row)
				return Dict[0]

		return None

	'''
		deletes the user, identified by their userid, from the database
	'''
	def removeUser(self, userid):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			cur.execute("DELETE FROM TBL_USERS WHERE id="+str(userid));
			return True

		return False		


	'''
		returns the records of a specific host site identified by the hostSiteID
	'''
	def getCoordinatorList(self,hostSiteID_int):
		return  rows_ArrDict
 		
	'''
		returns the login credentials, username and password, from the database
	'''
	def getLogin(self,user_Str, pass_Str):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#Check if HostSite Exists
			## Add HostSite to Table
			cur.execute("SELECT * FROM TBL_USERS WHERE email=\'"+user_Str+"\' and hashword=\'"+pass_Str+"\';");
			records=cur.fetchall()

			if(len(records)>0):
				#Returns First Row if any Exist (This is the User)
				return records[0]

		return None


	#############
	#Host Site Functions
	#############

	'''
		returns true if the given host site name exists within the database and false if it does not
	'''
	def hostSiteNameExists(self, name_str):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#Check if HostSite Exists
			## Add HostSite to Table
			cur.execute("SELECT name FROM TBL_HOSTSITES WHERE name=\'"+name_str+"\'");
			records=cur.fetchall()

			if(len(records)>0):
				return True

		return False


	'''
		creates a new host site with the given information
	'''
	#Conflicting Schema with Function, Hours = None, Email = None. For this Demo.
	#Add Coord Relationship Here aswell as in User
	def addHostSite(self,name_str, address_str, city_str, province_str,postalCode_str, coordinatorIDs_iAr, hoursOfOperation_Dict):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		print ("WE ARE HERE! POSTAL=")

		with con:

			cur = con.cursor()
			if(not self.hostSiteNameExists(name_str)):
				##Check if HostSites in our List exist
				#If a "non empty" HostSite list was passed
				if(coordinatorIDs_iAr is not None):
					for x in range (len(coordinatorIDs_iAr)):
						# If the Host Site Does not exist in the DB return false
						if ( self.getUser(coordinatorIDs_iAr[x]) == None ):
							print "Add User FAILED: A Link was attempted with a non-existing Host Site"
							return False


				## Add User to Table
				cur.execute("INSERT INTO TBL_HOSTSITES VALUES (null,\'"+name_str+"\',\'"+address_str+"\',\'"+city_str+"\',\'"+province_str+"\',\'"+postalCode_str+"\',null,null)");

				#Grab Added HOSTSITE ID
				cur.execute("SELECT * FROM TBL_HOSTSITES WHERE name=\'"+name_str+"\'");
				record=cur.fetchall()
				print str(record[0][0])
				
				## Update Hostsite(s) Rel with this User
				if(coordinatorIDs_iAr is not None and record>0):
					for x in range (len(coordinatorIDs_iAr)):			
						cur.execute("INSERT INTO TBL_COORDINATOR_HOSTSITE_REL VALUES (null,"+str(coordinatorIDs_iAr[x])+","+str(record[0][0])+")");
				print "Success!"
				return True
		print "ADDING HOSTSITE:FAILED"
		return False


	'''
		updates the information of an existing host site with the given information. the host site is identified by the hostSiteID
	'''
	def updateHostSite(self,hostSiteID_int,name_str, address_str, city_str, province_str,postalCode_str, coordinatorIDs_iAr, hoursOfOperation_Dict):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		postalCode_str.replace(" ", "")
		print ("WE ARE HERE! POSTAL="+postalCode_str)


		#HotFix for PostalCode 




		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			#cur.execute("DELETE FROM TBL_ORDERS WHERE id="+str(orderID_i));
			cur.execute("UPDATE TBL_HOSTSITES SET name=\'"+name_str+"\', address=\'"+address_str+"\',city=\'"+city_str+"\',province=\'"+province_str+"\',postal_code=\'"+postalCode_str+"\' WHERE id="+str(hostSiteID_int)+";"); 
			return True

		return False


	'''
		deletes the host site identified by the hostSiteId from the database
	'''
	def removeHostSite(self,hostSiteID_int):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			cur.execute("DELETE FROM TBL_HOSTSITES WHERE id="+str(hostSiteID_int));
			return True

		return False

	'''
		returns all host sites belonging to a given coordinator identified by its coordinatorID.
	'''
	def getHostSiteList(self,coordinatorID_i): 

		return ArrDict

	'''
		returns the host site identified by its hostSiteID
	'''
	def getHostSite(self,hostSiteID_i):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		with con:

			cur = con.cursor()

			##Check if HostSites in our List exist
			cur.execute("SELECT * FROM TBL_HOSTSITES WHERE id="+str(hostSiteID_i));

			Dict = cur.fetchall()
			if(len(Dict)>0):
				#Return the first Row (The Only Row)
				return Dict[0]

		return None

	'''
		returns the records of all the host sites in the database.
	'''
	def getAllHostSites(self):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		with con: 

			cur = con.cursor()

			##Check if HostSites in our List exist
			cur.execute("SELECT * FROM TBL_HOSTSITES");

			records = cur.fetchall()
			if(len(records)>0):
				return records

		return None	


	#############
	#Order Functions
	#############

	'''
		creates a new order with the given parameters
	'''
	def createNewOrder(self,dateCreated_str, dateToDistribute_str, firstName_str, lastName_str, email_str, phoneNumber_str, shouldSendNotifications_bool, smallBoxQuantity_i,largeBoxQuantity_i, donations_decimal, donationReceipt_bool, address_Dict, totalPaid_decimal, hostSitePickupID_i, hostSiteOrderID_i, vouchers_iArr): 
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:

			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			if( self.getHostSite(hostSitePickupID_i) is not None):
				##Check if HostSites in our List exist

				## Add Order to Table, Ben I hate you for making me put 17 parameters in a function =_=
				#REciept HardCoded to False
				if(donationReceipt_bool):
					cur.execute("INSERT INTO TBL_ORDERS VALUES (null,\'"+dateCreated_str+"\',\'"+dateToDistribute_str+"\',\'"+firstName_str+"\',\'"+lastName_str+"\',\'"+email_str+"\',\'"+ phoneNumber_str+"\',\' 1 \',\'"+str(largeBoxQuantity_i)+"\',\'"+str(smallBoxQuantity_i)+"\',"+str(donations_decimal)+",\' 0 \',\'"+str(totalPaid_decimal)+"\',"+str(hostSitePickupID_i)+","+str(hostSiteOrderID_i)+");")
				else:
					cur.execute("INSERT INTO TBL_ORDERS VALUES (null,\'"+dateCreated_str+"\',\'"+dateToDistribute_str+"\',\'"+firstName_str+"\',\'"+lastName_str+"\',\'"+email_str+"\',\'"+ phoneNumber_str+"\',\' 0 \',\'"+str(largeBoxQuantity_i)+"\',\'"+str(smallBoxQuantity_i)+"\',"+str(donations_decimal)+",\' 0 \',\'"+str(totalPaid_decimal)+"\',"+str(hostSitePickupID_i)+","+str(hostSiteOrderID_i)+");")

				print "ORDER ADDED:Success!"
				return True
		print "ADDING ORDER:FAILED"
		return False

	'''
		updates an existing order with the information given
	'''
	def updateOrder(self,orderID_i, dateCreated_str, dateToDistribute_str, firstName_str, lastName_str, email_str, phoneNumber_str, shouldSendNotifications_bool, smallBoxQuantity_i,largeBoxQuantity_i, donations_decimal, totalPaid_decimal, hostSitePickupID_i, hostSiteOrderID_i, vouchers_iArr):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');
		print ("WE ARE HERE!")
		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			#cur.execute("DELETE FROM TBL_ORDERS WHERE id="+str(orderID_i));
			cur.execute("UPDATE TBL_ORDERS SET distribution_date=\'"+dateToDistribute_str+"\', creation_date=\'"+dateCreated_str+"\',customer_first_name=\'"+firstName_str+"\', customer_last_name=\'"+lastName_str+"\',customer_email=\'"+email_str+"\',customer_phone=\'"+phoneNumber_str+"\',email_notifications=0,large_quantity=\'"+str(largeBoxQuantity_i)+"\',small_quantity=\'"+str(smallBoxQuantity_i)+"\',donation=\'"+str( donations_decimal)+"\',donationReceipt=0,total_paid=\'"+str(totalPaid_decimal)+"\',hostsitepickup_idFK=\'"+hostSitePickupID_i+"\',hostsitecreated_idFK=\'"+hostSitePickupID_i+"\' WHERE id = "+orderID_i+";");		
			return True

		return False

	'''
		deletes the order, identified by the orderID, from the database
	'''
	def removeOrder(self,orderID_i): 
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			cur.execute("DELETE FROM TBL_ORDERS WHERE id="+str(orderID_i));
			return True

		return False

	'''
		marks the order, identified by the orderId, as cancelled
	'''
	def cancelOrder(self,orderID_i): 
		return Boolean


	'''
		returns the records of all the orders identified by being within the given start and end dates
	'''
	def getAllOrdersByDistributionDate(self,beginDate_str, endDate_str):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			cur.execute("SELECT * FROM TBL_ORDERS WHERE creation_date> \'"+beginDate_str+"\' AND creation_date< \'"+ endDate_str+"\';")
			records = cur.fetchall()
			return records
		return None

	'''
		returns the records of all the orders that have not been paid for identified by being within the given start and end dates
	'''
	def getAllUnpaidOrdersByDistributionDate(self,beginDate_Str, endDate_str): 
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			cur.execute("SELECT * FROM TBL_ORDERS WHERE total_paid=0 AND creation_date> \'"+beginDate_Str+"\' AND creation_date< \'"+ endDate_str+"\';")
			records = cur.fetchall()
			return records

		return None

	'''
		returns the records of all the orders that are cancelled identified by being within the given start and end dates
	'''
	def getAllCanceledOrdersByDistributionDate(self,beginDate_str, endDate_str):
		return ArrDict
	def getAllPaidOrdersByDistributionDate(self,beginDate_str, endDate_str):
		#Make sure mysql is running...duh
		con = mdb.connect('localhost', 'root', 'password', 'gardenfreshbox');

		with con:
			cur = con.cursor()
			#If the HostSites BOTH Exist (even if its the same one for both)
			cur.execute("SELECT * FROM TBL_ORDERS WHERE total_paid>0 AND creation_date> \'"+beginDate_str+"\' AND creation_date< \'"+ endDate_str+"\';")

			records = cur.fetchall()
			return records

		return None


	'''
		returns the records of the orders identified by belonging to a given host site and being within the given start and end dates
	'''

	def getOrderByDistributionDate(self,hostSiteID_i, beginDate_str, endDate_Stre): 
		return ArrDict	
	
	'''
		returns the records of all the orders that are unpaid, belonging to a given host site, 
		and identified by being within the given start and end dates
	'''
	def getUnpaidOrdersByDistributionDate(self,hostSiteID_i, beginDate_str, endDate_Stre): 
		return ArrDict









#gfb=GFBDatabaseController() ;


#Works: Adding a user with no hostsite
'''
gfb.addUser("iheartpickles@mail.com","password","Bob","Pickels","905-Mix-Alot", None, 1);
'''

#Works: Adding a hostsite with no Users 
'''
gfb.addHostSite("Uncle Bens", "221B Baker Street", "London", "On","B4TM4N", None, None)
'''

#Works: Adding a user with MultipleHostSites
'''
gfb.addHostSite("Uncle Bens", "221B Baker Street", "London", "On","B4TM4N", None, None)
gfb.addHostSite("Some Other Place", "221B Baker Street", "London", "On","B4TM4N", None, None)
hostSite_IDs =[1,2]
gfb.addUser("iheartTHEBESTpickles@mail.com","password","Bob","Pickels","905-Mix-Alot", hostSite_IDs, 1);
'''

#WORKING: Adding a HostSite with Multiple Users
'''
gfb.addUser("iheartTHEBESTpickles@mail.com","password","Bob","Pickels","905-Mix-Alot", None, 1);
gfb.addUser("iNotSoMuch@mail.com","password","Bob","Pickels","905-Mix-Alot", None, 1);
users = [1,2]
gfb.addHostSite("Uncle Bens", "221B Baker Street", "London", "On","B4TM4N", users, None)
'''


#WORKING: Adding an Order
'''
gfb.addHostSite("Uncle Bens", "221B Baker Street", "London", "On","B4TM4N", None, None)
#shouldSendNotifications_bool=First Bool  DonReciept=Second Bool
#Address Dict = NONE
addressDict=None
donationsReciept=False
totalPaid=0.00
donation=0.01
smallBox=0
largeBox=0
sendNotifs=False
hostSitePickUp=1
hostSiteOrder=1
voucher=None

gfb.createNewOrder("1992-12-30", "1992-12-31","Bob","Pickels","iheartTHEBESTpickles@mail.com","905-Mix-Alot",sendNotifs,smallBox,largeBox, donation, donationsReciept, addressDict,totalPaid,hostSitePickUp,hostSiteOrder,voucher) 

#YYYY-MM-DD
'''

#WORKING: Delete An Order
'''
gfb.addHostSite("Uncle Bens", "221B Baker Street", "London", "On","B4TM4N", None, None)
#shouldSendNotifications_bool=First Bool  DonReciept=Second Bool
#Address Dict = NONE
addressDict=None
donationsReciept=False
totalPaid=0.01
donation=0.01
smallBox=0
largeBox=0
sendNotifs=False
hostSitePickUp=1
hostSiteOrder=1
voucher=None

gfb.createNewOrder("1992-12-30", "1992-12-31","Bob","Pickels","iheartTHEBESTpickles@mail.com","905-Mix-Alot",sendNotifs,smallBox,largeBox, donation, donationsReciept, addressDict,totalPaid,hostSitePickUp,hostSiteOrder,voucher) 
gfb.removeOrder(7)
#YYYY-MM-DD
'''

#WORKING: Pull All Orders By Date Range
'''
rows=gfb.getAllUnpaidOrdersByDistributionDate("1900-01-01","2000-01-01")
for row in rows:
	print str(row)
'''
