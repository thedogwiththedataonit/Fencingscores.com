import pymongo 
from pymongo import MongoClient
import certifi
import gc

#Use this script to reference the main application.py file

#create a function that takes the name and category as parameters
#return the values and assign them to global so they can be reffered to in application.py

#The goal is to have a function that queries the results while
#categorizing the data into every category dictionary
#then everytime we switch from a category to another, it is not 
#querying the data and sorting again, but using the saved dictionaries from memory to
#reference it and make it more efficient.

def query_results(usr, cat):
    #print(category)
    cluster = MongoClient("mongodb+srv://thomas:0806@cluster0.2kcsq.mongodb.net/python?retryWrites=true&w=majority", tlsCAFile=certifi.where()) #MAC LINE
    db = cluster["Names_Cluster"]
    collection = db["Names"]

    #print(collection.distinct("Name"))

    name_document = collection.find_one({"Name":usr})
    win_percentage = round((name_document.get('Pool_win_percentage') * 100),2) 
    
    
    attended_comps = name_document.get('Competitions')
    attended_sorted_comps = sorted(attended_comps, key=lambda x: int(x.split(", ")[-1]))
    attended_cats = name_document.get("Category")
    

    club = name_document.get("Club")
    nation = name_document.get("Nation")

    all_comps = []
    cadet = []
    junior = []
    div1 = []
    div2 = []
    div3 = []

    list_weapons = []

    for category in attended_cats:
        if category[-1] == "E":
            list_weapons.append("Epee")
        if category[-1] == "F":
            list_weapons.append("Foil")
        if category[-1] == "S":
            list_weapons.append("Saber")

        #print(category)
        db_comp = cluster[category]
        collection_names_in_category = list(db_comp.list_collection_names())
        #print(collection_names_in_category)
        for comp in attended_sorted_comps:#list of all competitions
            if comp in collection_names_in_category:
            
                if "Cadet" in comp:
                    
                    collection_comp = db_comp[comp] #try... checks if the competition exists within the cluster

                    #print(comp)
                    fencer_document = collection_comp.find_one({"Name":usr})
                    #print(fencer_document)
                    #print("___________________________")

                    all_comps.append(fencer_document)
                    cadet.append(fencer_document)
                    #print(win_fencers)

                        
                if "Junior" in comp:

                    collection_comp = db_comp[comp] #try... checks if the competition exists within the cluster
                    #print(comp)
                    fencer_document = collection_comp.find_one({"Name":usr})
                    #print(fencer_document)
                    #print("___________________________")

                    all_comps.append(fencer_document)
                    junior.append(fencer_document)

                if "Div I" in comp:

                    collection_comp = db_comp[comp] #try... checks if the competition exists within the cluster


                    #print(comp)
                    fencer_document = collection_comp.find_one({"Name":usr})
                    #print(fencer_document)
                    #print("___________________________")

                    all_comps.append(fencer_document)
                    div1.append(fencer_document)

            else:
                continue
    #print(all_comps)
    
    list_weapons = list(dict.fromkeys(list_weapons))
    if (cat == "all"): #WTF THE TITLES DONT LINE UP BUG BUG BUG
        return (usr, 
                win_percentage, 
                club, 
                len(club), 
                nation,
                                
                all_comps,
                list_weapons,
                )   
    if cat == "cadet":
        return (usr, 
                win_percentage, 
                club, 
                len(club), 
                nation,

                cadet,
                list_weapons,
                )   
    if cat == "junior":
        return (usr, 
                win_percentage, 
                club, 
                len(club), 
                nation,
                
                junior,
                list_weapons,
                )
    if cat == "div1":
        return (usr,                        #0
                win_percentage,             #1 
                club,                       #2
                len(club),                  #3
                nation,                     #4

                div1,                       #5
                list_weapons,
                ) 

    holder_variable = "NA"
    if (cat == "y14") or (cat == "div2") or (cat == "div3"):
        return (usr,                        #0
                win_percentage,             #1 
                club,                       #2
                len(club),                  #3
                nation,                     #4
                holder_variable,            #5
                list_weapons,             
                )


#results = (query_results("PARK THOMAS JUNSEO", "all"))
#print(results)
#print(len(results[5]["win_fencer_len"]))
#print(len(results[5]["win_score_list"]))
#print((results[5]["len_attended_comps"]))

 #RETURNS ARE BY INDEX VALUES

