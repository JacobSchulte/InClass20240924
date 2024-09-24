# dictionaries.py

def demo():
    """
    Demonstrate basic dictionary stuff
    """
    myDictionary = myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)

    #iterate over the dictionary by key 
    for key in myDictionary.keys():
        print(key)

    # Iterate by key/value
    for item in myDictionary.items():
        print(item)

    #Iterate by value 
    for value in myDictionary.values():
        print(value)

    #Add a key/value pair
    myDictionary["Louisville"] = "Cardinals"

    print(len(myDictionary))

    #Cause an exception. Add try/except logic 
    #to gracefully handle this
    try:
        print(myDictionary["University of Kentucky"])
    except: 
        #We end up here if an exception is thrown
        # in the try block
        print("UK does not exist here")
    
    #Remove Xavier by key and print the entire dictionary

    myDictionary.pop("Xavier")
    print(myDictionary)
       
    # Create another Dictionary called newtTeams.
    # Add several key/value pairs
    # Combine that with myDictionary and print the results

    newTeams = {"Boston University":"Terriers", "Maryland":"Terrapins", "Florida":"Gators"}

    myDictionary.update(newTeams)
    print(myDictionary)


