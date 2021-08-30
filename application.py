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



@application.route("/<usr>")
def user(usr):
    
    cluster = MongoClient("mongodb+srv://thomas:0806@cluster0.2kcsq.mongodb.net/python?retryWrites=true&w=majority", tlsCAFile=certifi.where()) #MAC LINE
    db = cluster["Names_Cluster"]
    collection = db["Names"]

    name_document = collection.find_one({"Name":usr})
    win_pre = (name_document.get('Pool_win_percentage') )
    win_p = round(win_pre, 2) * 100
    win_percentage = str(win_p) + "%"
        
    attended_comps = name_document.get('Competitions')
    attended_cats = name_document.get("Category")

    club = name_document.get("Club")
    nation = name_document.get("Nation")

        #How do I send pool data?? DEFINE WIN LOSS BEFORE SO ITS IN MONGODB
    win_fencers_list = []
    win_scores_list = []
    win_list_len = []

    loss_fencers_list = []
    loss_scores_list = []
    loss_list_len = []

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

                win_scores = fencer_document.get('win_scores')
                win_list_len.append(len(win_scores))
                win_scores_list.append(win_scores)

                    

                loss_fencers = fencer_document.get('loss_fencers')
                loss_fencers_list.append(loss_fencers)

                loss_scores = fencer_document.get('loss_scores')
                loss_list_len.append(len(loss_scores))
                loss_scores_list.append(loss_scores)
            except:
                continue

        

    print(win_list_len)
        


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

                                )
   

if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment
