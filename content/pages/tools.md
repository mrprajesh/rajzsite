Title: Tools
Date: 20.12.2017 15:15:38
page-order: 4
 
#Graph Projects [outdated!]
Dynamic Graph - A small step towards visualization
	* Click to [launch][1]
	* _Note:_ Runs on Java v1.7 or greater; In Linux this plugin may be needed `sudo apt-get install icedtea-plugin`. 


#Under graduate - Projects 

## TCE SMS 
Publishing Exam results through SMS(Short Message Service) using a GSM 
(Global System for Mobile Communications) Modem. 
It is an auto responding application developed using Java communication API's developed by Sun Microsystems. 
Using communication [API][3] and invoking appropriate [AT][4] commands from/to GSM modem to read the received message 
and retrieving the appropriate response from postgreSQL database (where exam results are stored) 
then wrap it into a well defined format and replied as SMS to the student.

## Manage Prisons
We Team Resilience (sooria, vivek, myself & ap) won 2nd runners up - 
The Great Mind Challenge(TGMC) 2008, a National level contest by IBM 
and had made it to the TGMC Hall of fame. [more][2]

## E-COPs
Our team won 2nd runners up succesively - The Great Mind Challenge(TGMC) 2009, National level contest by IBM. //TODO add [more][2]

## Online Fleet Management system using Global Positioning System.
It includes live tracking of vehicles fitted with GPS module([GM862 Evaluation Kit][5] is used for demonstration) 
through the web interface. It uses Google Maps API's. 
The Telit GPS module inside the kit is configured using Python. 
It get the GPS coordinates at a regualar interval and sends it to the web server through HTTP request 
(using GPRS available in the modem). It can send SMS alerts to the registered mobile on reaching specified locations using the GSM module in the kit(and Reverse Geocoding). 
Ofcourse, kit should have a dedicated SIM installed in it with GPRS/SMS capability. 
Apart from this, as a daily activity report generation plays a prominent role in recording the whereabouts of the vehicles. 
It is generated using [Jasper Reports][6]. 

[1]: http://www.cse.iitm.ac.in/~mrprajesh/oldWebsite/java/dynamic_graph.jnlp
[2]: http://www-07.ibm.com/in/university/greatmind/tgmc_halloffame.html
[3]: http://www.cse.iitm.ac.in/~mrprajesh/oldWebsite/comm3.0_u1_linux.zip
[4]: https://en.wikipedia.org/wiki/Hayes_command_set
[5]: https://www.sparkfun.com/products/retired/280
[6]: https://en.wikipedia.org/wiki/JasperReports
