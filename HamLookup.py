import collections

callsigndata = ["N4CJP, Chris Pappas, Shepherdstown-WV, General", "N3WJP, Jason Pappas, Shepherdstown-WV, Extra", "WX4MET, Sarah Pappas, Shepherdstown-WV, General", 
                "KB3ARZ, Bob White, Indian Head-MD, Technician", "W8NO, Brad Hess, Nanjemoy-MD, Extra", "AE7YH, John Royo, Winchester-VA, Extra"]
callsigns = {"N4CJP, N3WJP, WX4MET, KB3ARZ, W8NO, AE7YH"}

print("Callsign Lookup (Callsign, Name, Location, Class)")
lookup = input("Enter Callsign:")

for item in callsigndata:
        if lookup in item:
            print(item)
        


########## POST PROJECT REPORT
# My goal initially was to pull all Callsign information for all licensees straight from the FCC or QRZ.com, instead of building my own database of a handful of callsigns.
# While not being super great at programming in general, I have never used APIs or web integration and have no experience and don't understand it. It was super ambitious, thus I
# shifted my focus to building a database, where it will still return the results of the initial goal (Name, Callsign, Class, and location). The user is able to input a callsign and
# it will return them the desired information from a dataset. The input will lookup the given data through that set, and if it matches a callsign in the database, it will return
# the callsign with the given information. My main struggle at first was how I wanted to structure the database to present the information, I decided the best would be a list. And each
# element would be the respective information in order. The order given to the user when prompted to input a callsign. (Callsign Lookup: (Callsign, Name, Location, Class)). Another
# difficulty is just inputting all the data. The FCC stopped issuing some of the APIs, and some they do don't offer the information needed; and QRZ you have to pay for and login inorder
# access. Thus not making the program feasible for the general use. If the API was able to be integrated, it would make searching alot easier, and would save the programmer from
# a lot of writing. Additionally, as my list grows, the more data it'll take, the longer it'll take to search, and the more in efficient it'll be. If I had the skills I would've used 
# the API that would save alot of time and energy, or even have it pull from and SQL database or build my own, which would be much more efficient.

