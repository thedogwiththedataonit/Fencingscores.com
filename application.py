from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import redirect
import pymongo 
from pymongo import MongoClient
import certifi



application = Flask(__name__)

@application.route('/', methods=["POST","GET"])
def main():
    if request.method == "POST": #IMPROVE SEARCH FUNCTION
        user = request.form["nm"]

        cluster = MongoClient("mongodb+srv://thomas:0806@cluster0.2kcsq.mongodb.net/python?retryWrites=true&w=majority", tlsCAFile=certifi.where()) #MAC LINE
        db = cluster["Names_Cluster"]
        collection = db["Names"]
        cap_usr = user.upper()

        try:
            name_document = collection.find_one({"Name":cap_usr})
            win_pre = (name_document.get('Pool_win_percentage') )

            return redirect(url_for("user", usr=cap_usr))
        except:
            return render_template('index.html', error="No Name")

    else:
        return render_template('index.html')


@application.route("/<usr>", methods=["POST","GET"]) #HOW TO CONTINUE URLS / / /
def user(usr):
    
    cluster = MongoClient("mongodb+srv://thomas:0806@cluster0.2kcsq.mongodb.net/python?retryWrites=true&w=majority", tlsCAFile=certifi.where()) #MAC LINE
    db = cluster["Names_Cluster"]
    collection = db["Names"]

    name_document = collection.find_one({"Name":usr})
    win_pre = name_document.get('Pool_win_percentage')
    win_p = round(win_pre, 2) * 100
    win_percentage = str(win_p) + "%"
        
    attended_comps = name_document.get('Competitions')
    attended_cats = name_document.get("Category")

    club = name_document.get("Club")
    nation = name_document.get("Nation")

    #Organize by competition category within the python call, so sort the competitions by category, all values, including wins score etc

    win_fencers_list = []
    win_scores_list = []
    win_list_len = []

    loss_fencers_list = []
    loss_scores_list = []
    loss_list_len = []
    indicator_list = []
    touch_scored_list = []
    touch_rec_list = []


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

    y14 = {
        "attended_comps": [],
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_scores_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }

    cadet = {
        "attended_comps": [],
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_scores_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }

    junior = {
        "attended_comps": [],
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_scores_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }

    div1 = {
        "attended_comps": [],
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_scores_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }

    div2 = {
        "attended_comps": [],
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_scores_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }

    div3 = {
        "attended_comps": [],
        "win_fencer_list": [],
        "win_fencer_len": [],
        "win_scores_list": [],
        "loss_fencer_list": [],
        "loss_fencer_len": [],
        "loss_score_list": [],
        "indicator_list": [],
        "touch_scored_list": [],
        "touch_rec_list": [],
    }


    #so far, use dictionaries to speciffy the types so if can be indexed and clicked upon

    #how do you add more apges and go deeper? <usr>/all or <usr>/y14
    #clicking on the additional url /## posts the information, so maybe a new function?

    for category in attended_cats:
        db_comp = cluster[category]

        for comp in attended_comps:
            
            try:
                  #MAKE DYNAMIC TO MORE CATEGORIES
                collection_comp = db_comp[comp]

                # print(comp)
                fencer_document = collection_comp.find_one({"Name":usr})
                #print(fencer_document)

                win_fencers = fencer_document.get('win_fencers')
                #print(win_fencers)
                
                win_fencers_list.append(win_fencers)
                all_comps["win_fencer_list"].append(win_fencers)

                win_scores = fencer_document.get('win_scores')
                win_list_len.append(len(win_scores))
                all_comps["win_fencer_len"].append(len(win_scores))

                win_scores_list.append(win_scores)
                all_comps["win_score_list"].append(win_scores)

                loss_fencers = fencer_document.get('loss_fencers')
                loss_fencers_list.append(loss_fencers)
                all_comps["loss_fencer_list"].append(loss_fencers)

                loss_scores = fencer_document.get('loss_scores')
                loss_list_len.append(len(loss_scores))
                all_comps["loss_fencer_len"].append(len(loss_scores))

                loss_scores_list.append(loss_scores)
                all_comps["loss_score_list"].append(loss_scores)

                indicator = fencer_document.get('Indicator')
                indicator_list.append(indicator)
                all_comps["indicator_list"].append(indicator)

                touch_scored = fencer_document.get("Total_scored")
                touch_scored_list.append(touch_scored)
                all_comps["touch_scored_list"].append(touch_scored)

                touch_rec = fencer_document.get("Total_Received")
                touch_rec_list.append(touch_rec)
                all_comps["touch_rec_list"].append(touch_rec)

            except:
                continue

        

    
        

    #USE DICTIONARIESSS!!!!!!


    #print(all_comps)
    return render_template('profile.html', 
                                name=usr, 
                                win_percentage=win_percentage, 
                                len=len(attended_comps), 
                                attended_comps=attended_comps, 
                                club=club, 
                                club_len=len(club), 
                                nation=nation,
                                
                                win_fencers_list = win_fencers_list,
                                win_list_len = win_list_len,
                                win_scores_list = win_scores_list,

                                loss_fencers_list = loss_fencers_list,
                                loss_list_len = loss_list_len,
                                loss_scores_list = loss_scores_list,

                                indicator_list = indicator_list,
                                touch_scored_list = touch_scored_list,
                                touch_rec_list = touch_rec_list,
                                
                                all_comps=all_comps
                                )



if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment
