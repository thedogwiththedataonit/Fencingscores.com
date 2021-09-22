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

    name_document = collection.find_one({"Name":usr})
    win_percentage = name_document.get('Pool_win_percentage')
    
        
    attended_comps = name_document.get('Competitions')
    attended_cats = name_document.get("Category")

    club = name_document.get("Club")
    nation = name_document.get("Nation")

    all_comps = {
        "attended_comps": attended_comps,
        "len_attended_comps": len(attended_comps),
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_score_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }
    cadet = {
        "attended_comps": [],
        "len_attended_comps": 0,
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_score_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }
    junior = {
        "attended_comps": [],
        "len_attended_comps": 0,
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_score_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }
    div1 = {
        "attended_comps": [],
        "len_attended_comps": 0,
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_score_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }
    div2 = {
        "attended_comps": [],
        "len_attended_comps": 0,
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_score_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }
    div3 = {
        "attended_comps": [],
        "len_attended_comps": 0,
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_score_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }

    for category in attended_cats:
        #print(category)
        db_comp = cluster[category]

        for comp in attended_comps: #list of all competitions
            try:

                collection_comp = db_comp[comp] #try... checks if the competition exists within the cluster


                #print(comp)
                fencer_document = collection_comp.find_one({"Name":usr})
                #print(fencer_document)
                #print(fencer_document)
                title = fencer_document.get('Title')   
                #print(title)

                win_fencers = fencer_document.get('win_fencers')
                all_comps["win_fencer_list"].append(win_fencers)
                #print(win_fencers)

                win_scores = fencer_document.get('win_scores')
                len_win_scores = len(win_scores)
                all_comps["win_fencer_len"].append(len_win_scores)
                #print(len_win_scores)
                all_comps["win_score_list"].append(win_scores)
                #print(win_scores)

                loss_fencers = fencer_document.get("loss_fencers")
                all_comps["loss_fencer_list"].append(loss_fencers)
                #print(loss_fencers)

                loss_scores = fencer_document.get('loss_scores')
                len_loss_scores = len(loss_scores)
                all_comps["loss_fencer_len"].append(len_loss_scores)
                all_comps["loss_score_list"].append(loss_scores)
                #print(loss_scores)

                indicator = fencer_document.get('Indicator')
                all_comps["indicator_list"].append(indicator)
                #print(indicator)

                touch_scored = fencer_document.get('Total_scored')
                all_comps["touch_scored_list"].append(touch_scored)
                #print(touch_scored)

                touch_rec = fencer_document.get('Total_Received')
                all_comps["touch_rec_list"].append(touch_rec)
                #print(touch_rec)

                if "Cadet" in title:
                    
                    cadet["attended_comps"].append(title)
                    cadet["len_attended_comps"] = cadet["len_attended_comps"] + 1
                    cadet["win_fencer_list"].append(win_fencers)
                    cadet["win_fencer_len"].append(len_win_scores)
                    cadet["win_score_list"].append(win_scores)

                    cadet["loss_fencer_list"].append(loss_fencers)
                    cadet["loss_fencer_len"].append(len_loss_scores)
                    cadet["loss_score_list"].append(loss_scores)

                    cadet["indicator_list"].append(indicator)
                    cadet["touch_scored_list"].append(touch_scored)
                    cadet["touch_rec_list"].append(touch_rec)
                    
                if "Junior" in title:
                    junior["attended_comps"].append(title)
                    junior["len_attended_comps"] = junior["len_attended_comps"] + 1
                    junior["win_fencer_list"].append(win_fencers)
                    junior["win_fencer_len"].append(len_win_scores)
                    junior["win_score_list"].append(win_scores)

                    junior["loss_fencer_list"].append(loss_fencers)
                    junior["loss_fencer_len"].append(len_loss_scores)
                    junior["loss_score_list"].append(loss_scores)

                    junior["indicator_list"].append(indicator)
                    junior["touch_scored_list"].append(touch_scored)
                    junior["touch_rec_list"].append(touch_rec)

                if "Div I" in title:
                    div1["attended_comps"].append(title)
                    div1["len_attended_comps"] = div1["len_attended_comps"] + 1
                    div1["win_fencer_list"].append(win_fencers)
                    div1["win_fencer_len"].append(len_win_scores)
                    div1["win_score_list"].append(win_scores)

                    div1["loss_fencer_list"].append(loss_fencers)
                    div1["loss_fencer_len"].append(len_loss_scores)
                    div1["loss_score_list"].append(loss_scores)

                    div1["indicator_list"].append(indicator)
                    div1["touch_scored_list"].append(touch_scored)
                    div1["touch_rec_list"].append(touch_rec)

            except:
                pass
    
    #print(all_comps)
    
    if (cat == "all"): #WTF THE TITLES DONT LINE UP BUG BUG BUG
        return (usr, 
                win_percentage, 
                club, 
                len(club), 
                nation,
                                    
                all_comps,
                )   
    if cat == "cadet":
        return (usr, 
                win_percentage, 
                club, 
                len(club), 
                nation,

                cadet,
                )
    
    if cat == "junior":
        return (usr, 
                win_percentage, 
                club, 
                len(club), 
                nation,

                junior,
                )
    if cat == "div1":
        return (usr,                        #0
                win_percentage,             #1 
                club,                       #2
                len(club),                  #3
                nation,                     #4

                div1,                       #5
                )
    
    if (cat == "y14") or (cat == "div2") or (cat == "div3"):
        return (usr,                        #0
                win_percentage,             #1 
                club,                       #2
                len(club),                  #3
                nation,                     #4

                             #5
                )


#results = (query_results("PARK THOMAS JUNSEO", "all"))
#print(results)
 #RETURNS ARE BY INDEX VALUES

