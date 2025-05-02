import requests

def pull_callsign(callsign):
    url = f"https://callook.info/{callsign}/json"
    # uses this website to pull data from using its API
    
    try:
        response = requests.get(url) # this is sending the API request
        response.raise_for_status() # this will give an error if the request doesn't go through
        data = response.json()

        if data.get("status") == "INVALID": # this will return if the callsign inputted doesn't exist
            print(f"Callsign '{callsign}' not found.")
            return None

        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# 🔎 User input
user_input = input("Enter Callsign: ").strip().upper() # this changes the formatting of the printed text

callsign_information = pull_callsign(user_input) # used for user to input a callsign

if callsign_information:
    print("\n Callsign Info:")
    print(f"Name: {callsign_information.get('name')}") # prints licensee's name
    print(f"Callsign: {callsign_information.get('current', {}).get('callsign')}") # prints licensees callsign
    print(f"License Class: {callsign_information.get('operclass')}") # prints the class the licensee holds (Technician, General, Extra)
    print(f"Location: {callsign_information.get('address', {}).get('line1', '')}, {callsign_information.get('address', {}).get('line2', '')}") # prints the licensees address
    print(f"Grid:{callsign_information.get('gridsquare', {}).get('gridsquare')}") #shows which grid they are in
    print(f"Latitude:{callsign_information.get('location', {}).get('latitude')}") # shows latitude coordinates of licensee
    print(f"Longitude:{callsign_information.get('location', {}).get('longitude')}") # shows longitude coordinates of licensee
    print(f"Expires:{callsign_information.get('expiryDate', {}).get('expiryDate')}") # shows when the license expires
else:
    print("Callsign Not Found") # if callsign doesn't exist




#
#----------------------------------------------POST PROJECT REPORT---------------------------------------------
#Title: Amateur Radio License Database Search
#Summary: To create a searchable database to pull information about a desired HAM Radio License by a user-inputted callsign
#Goals: To first create a user input to prompt to input a callsign. Then, use some sort of web tool or API to fetch data about that callsign from a database on the internet. 
#        Then publish and print the information to the user.
#        
#Did the project achieve its goals? Yes, I was able to make an input that allowed me to put a callsign in, and for it to return information from a website. If you'd like feel free to try any call sign.
#    My callsign is N4CJP, my dads is N3WJP, and my sisters is WX4MET
#    The only thing that wasn't really accomplished is some information I couldn't pull. The license class, grid square, and license expiration date. I am not sure why, I want to say it has something to
#    do with the API and requesting the information. If you search the callsigns on the website it shows the informtion. Here it shows everything except for those. I went to their API documentation and
#    even saw the keywords used for .get for those, used the same ones and they would not work. For instance, the license class would not show up whether I used "class" or "operClass"
