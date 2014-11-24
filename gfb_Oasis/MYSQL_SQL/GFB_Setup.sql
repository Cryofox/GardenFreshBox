drop database gardenfreshbox;
CREATE DATABASE gardenfreshbox;

use gardenfreshbox;


#HostSites
CREATE TABLE TBL_HOSTSITES
(
id int Not Null auto_increment primary key,
name varchar(255) unique,
address varchar(255),
city varchar(255),
province varchar(255),
postal_code varchar(6) ,
email varchar(255),
hoursOfOperation int
);

#Orders
CREATE TABLE TBL_ORDERS
(
id int Not Null AUTO_INCREMENT primary key,
creation_date date ,
distribution_date  date,
customer_first_name varchar(255),
customer_last_name varchar(255),
customer_email varchar(255),
customer_phone varchar(255),
email_notifications boolean ,
small_quantity int, 
large_quantity int,

donation decimal (10,2),
donationReceipt boolean, 
total_paid decimal (10,2),


hostsitepickup_idFK int, foreign key(hostsitepickup_idFK) REFERENCES TBL_HOSTSITES(id),
hostsitecreated_idFK int, foreign key(hostsitecreated_idFK) REFERENCES TBL_HOSTSITES(id)
);

#Credentials, User Types: Admin, Coord, Volunteer
CREATE TABLE TBL_CREDENTIALS
(
id int Not Null auto_increment primary key,
label varchar(255)
);

#Users
CREATE TABLE TBL_USERS
(
id int Not Null auto_increment primary key,
email varchar (255) Unique,
hashword  varchar (255),
first_name varchar (255),
last_name varchar(255),
phone_number varchar (255),
credentials_idFK int,foreign key(credentials_idFK) REFERENCES TBL_CREDENTIALS(id)
);

#Credentials, User Types: Admin, Coord, Volunteer
CREATE TABLE TBL_COORDINATOR_HOSTSITE_REL
(
id int Not Null auto_increment primary key,
user_idFK int,foreign key(user_idFK) REFERENCES TBL_USERS(id),
hostsite_idFK int, foreign key(hostsite_idFK) REFERENCES TBL_HOSTSITES(id)
);

Insert into tbl_credentials values(null,'admin');
Insert into tbl_credentials values(null,'coordinator');
Insert into tbl_credentials values(null,'volunteer');
