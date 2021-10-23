# covidBedAPI

## Setup

1. Have pip installed 

2. run `pip install -r requirements.txt`

3. Install MongoDB Compass

4. run api.py

5.  Run API calls. 

---
	
 _All the details, Sample Input and Sample response is in [Overview.txt](https://github.com/myNameArnav/covidBedAPI/blob/master/Overview.txt)_

---

## Overview

Populate beds:
	To populate the database with existing bookings

	- POST
		Returns "Populated" with a Response code of 201

Booked beds:
	To show already booked beds

	- GET
		Returns JSON with a Response code of 200

			// Sample Input

				http http:5000/api/booked_beds

			// Sample Response
			

				[
					{
						"_id": 1,
						"criticalLevel": "critical",
						"hospitalName": "Max",
						"pincode": 110099,
						"timeSlot": "06:00 - 09:00"
					}
				]


Book bed:
	To book bed with a time slot, name, id, critical level, hospital name, zipcode
	
	- POST
		Returns "Created" with a Response code of 201

		// Sample Input

			echo {"_id": 3, "criticalLevel": "Not Critical", "hospitalName": "Appolo", "pincode": 110042, "timeSlot": "15:00 - 18:00"} | http POST http://127.0.0.1:5000/api/book_bed


Reschedule:
	To change the time slot of the booking

	- GET
		Returns JSON with a Response code of 200/404

		// Sample Input

			http GET http://127.0.0.1:5000/api/reschedule/3

		// Sample Response

			[
				{
					"_id": 3,
					"criticalLevel": "Not Critical",
					"hospitalName": "Appolo",
					"pincode": 110042,
					"timeSlot": "15:00 - 18:00"
				}
			]

	- PUT
		Returns JSON with a Response code of 202

		// Sample Input

			echo {"_id": 3, "criticalLevel": "Not Critical", "hospitalName": "Appolo", "pincode": 110042, "timeSlot": "18:00 - 21:00"} | 
			http PUT http://127.0.0.1:5000/api/reschedule/3

		// Sample Response

			[
				{
					"_id": 3,
					"criticalLevel": "Not Critical",
					"hospitalName": "Appolo",
					"pincode": 110042,
					"timeSlot": "18:00 - 21:00"
				}
			]



Cancel:
	To cancel the booking of the bed

	- DELETE
		Returns "Deleted" with a Response code of 200
