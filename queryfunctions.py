from typing import List
import pymongo
from pymongo import MongoClient
import certifi
import gc
from mongo import connection_string
import random

# Use this script to reference the main application.py file

# create a function that takes the name and category as parameters
# return the values and assign them to global so they can be reffered to in application.py

# The goal is to have a function that queries the results while
# categorizing the data into every category dictionary
# then everytime we switch from a category to another, it is not
# querying the data and sorting again, but using the saved dictionaries from memory to
# reference it and make it more efficient.


def query_results(usr, cat):
    # print(category)
    cluster = MongoClient(
        connection_string, tlsCAFile=certifi.where())  # MAC LINE
    db = cluster["Names_Cluster"]
    collection = db["Names"]

    # print(collection.distinct("Name"))

    name_document = collection.find_one({"Name": usr})
    win_percentage_list = name_document.get('Pool_win_percentage')
    win_percentage_sum = sum(win_percentage_list)
    print(win_percentage_sum)
    win_percentage = (
        round(((win_percentage_sum) / len(win_percentage_list)), 2)) * 100

    # FIX HERE, IT SORTS THEN PUSHES TO A ITERATION SORT BY CADET< JUNIOR DIV 1, SHOULD SORT BY DATE AFTER FOR JS CHART
    attended_comps = name_document.get('Competitions')
    attended_sorted_comps = sorted(
        attended_comps, key=lambda x: int(x.split(", ")[-1]))
    # print(attended_sorted_comps)
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

        # print(category)
        db_comp = cluster[category]
        collection_names_in_category = list(db_comp.list_collection_names())
        # print(collection_names_in_category)
        for comp_title in attended_sorted_comps:  # list of all competitions
            # print(comp_title)

            if ("Cadet" in comp_title) and (comp_title in collection_names_in_category):

                # try... checks if the competition exists within the cluster
                collection_comp = db_comp[comp_title]

                # print(comp_title)
                fencer_document = collection_comp.find_one({"Name": usr})
                # print(fencer_document)
                # print("___________________________")

                all_comps.append(fencer_document)
                cadet.append(fencer_document)
                # print(win_fencers)
                continue

            if ("Junior" in comp_title) and (comp_title in collection_names_in_category):

                # try... checks if the competition exists within the cluster
                collection_comp = db_comp[comp_title]
                # print(comp_title)
                fencer_document = collection_comp.find_one({"Name": usr})
                # print(fencer_document)
                # print("___________________________")

                all_comps.append(fencer_document)
                junior.append(fencer_document)
                continue

            if ("Div I" in comp_title) and (comp_title in collection_names_in_category):

                # try... checks if the competition exists within the cluster
                collection_comp = db_comp[comp_title]

                # print(comp_title)
                fencer_document = collection_comp.find_one({"Name": usr})
                # print(fencer_document)
                # print("___________________________")

                all_comps.append(fencer_document)
                div1.append(fencer_document)
                continue

            else:
                continue

    # print(all_comps)
    # resorting allcomps
    sorted_all_comps = sorted(
        all_comps, key=lambda x: attended_sorted_comps.index(x["Title"]))
    # print(sorted_all_comps)

    list_weapons = list(dict.fromkeys(list_weapons))
    if (cat == "all"):
        return (usr,
                win_percentage,
                club,
                len(club),
                nation,

                sorted_all_comps,
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
        return (usr,  # 0
                win_percentage,  # 1
                club,  # 2
                len(club),  # 3
                nation,  # 4

                div1,  # 5
                list_weapons,
                )

    holder_variable = "NA"
    if (cat == "y14") or (cat == "div2") or (cat == "div3"):
        return (usr,  # 0
                win_percentage,  # 1
                club,  # 2
                len(club),  # 3
                nation,  # 4
                holder_variable,  # 5
                list_weapons,
                )


#results = (query_results("PARK THOMAS JUNSEO", "all"))
# print(results)
# print(len(results[5]["win_fencer_len"]))
# print(len(results[5]["win_score_list"]))
# print((results[5]["len_attended_comps"]))

 # RETURNS ARE BY INDEX VALUES

def comp_data(comp):
    if (comp[0:16] == "Cadet Men's Epee"):
        comp_cat = "USFA_CME"
        comp_title = "Cadet Men's Epee"

    if (comp[0:17] == "Junior Men's Epee"):
        comp_cat = "USFA_JME"
        comp_title = "Junior Men's Epee"

    if (comp[0:16] == "Div I Men's Epee"):
        comp_cat = "USFA_DME"
        comp_title = "Div I Men's Epee"

    if (comp[0:18] == "Cadet Women's Epee"):
        comp_cat = "USFA_CWE"
        comp_title = "Cadet Women's Epee"

    if (comp[0:19] == "Junior Women's Epee"):
        comp_cat = "USFA_JWE"
        comp_title = "Junior Women's Epee"

    if (comp[0:18] == "Div I Women's Epee"):
        comp_cat = "USFA_DWE"
        comp_title = "Div I Women's Epee"

    if (comp[0:16] == "Cadet Men's Foil"):
        comp_cat = "USFA_CMF"
        comp_title = "Cadet Men's Foil"

    if (comp[0:17] == "Junior Men's Foil"):
        comp_cat = "USFA_JMF"
        comp_title = "Junior Men's Foil"

    if (comp[0:16] == "Div I Men's Foil"):
        comp_cat = "USFA_DMF"
        comp_title = "Div I Men's Foil"

    if (comp[0:18] == "Cadet Women's Foil"):
        comp_cat = "USFA_CWF"
        comp_title = "Cadet Women's Foil"

    if (comp[0:19] == "Junior Women's Foil"):
        comp_cat = "USFA_JWF"
        comp_title = "Junior Women's Foil"

    if (comp[0:18] == "Div I Women's Foil"):
        comp_cat = "USFA_DWF"
        comp_title = "Div I Women's Foil"

    if (comp[0:17] == "Cadet Men's Saber"):
        comp_cat = "USFA_CMS"
        comp_title = "Cadet Men's Saber"

    if (comp[0:18] == "Junior Men's Saber"):
        comp_cat = "USFA_JMS"
        comp_title = "Junior Men's Saber"

    if (comp[0:17] == "Div I Men's Saber"):
        comp_cat = "USFA_DMS"
        comp_title = "Div I Men's Saber"

    if (comp[0:19] == "Cadet Women's Saber"):
        comp_cat = "USFA_CWS"
        comp_title = "Cadet Women's Saber"

    if (comp[0:20] == "Junior Women's Saber"):
        comp_cat = "USFA_JWS"
        comp_title = "Junior Women's Saber"

    if (comp[0:19] == "Div I Women's Saber"):
        comp_cat = "USFA_DWS"
        comp_title = "Div I Women's Saber"

    cluster = MongoClient(
        connection_string, tlsCAFile=certifi.where())  # MAC LINE
    db = cluster[comp_cat]
    collection = db[comp]

    values_split = comp.split(comp_title)
    date = values_split[1]

    list_of_documents = list(collection.find())
    # print(list_of_documents)

    # print(list_of_documents[1]["Victory_count"])
    sort = sorted(list_of_documents, key=lambda k: (
        k["Victory_count"]), reverse=True)

    # print("-------------------------")
    # print(sort)
    # for i in sort:
    # print(i["Percentage_wins"])
    # print(i["Indicator"])
    # print(i["Name"])

    return (comp_title,
            date,
            sort,
            )


def top_fencer_names():
    cluster = MongoClient(
        connection_string, tlsCAFile=certifi.where())  # MAC LINE
    db = cluster["Names_Cluster"]
    collection = db["Names"]

    # GET AVERAGE OF THISSSSSS AND QUERY
    query = {"$and": [{"win_per_total": {"$gt": .90}},
                      {"Competitions.4": {"$exists": True}}]}

    # ONLY QUERY A DOCUMENT VALUE FROM A CONDITIONAL
    names = list(collection.find(query))

    names_list = []
    club_list = []
    for i in names:
        names_list.append(i["Name"])
        club_list.append(i["Club"][-1])

    combined = list(zip(names_list, club_list))

    random.shuffle(combined)

    names_list, club_list = zip(*combined)
    # print(names_list)
    # print(club_list)

    return (names_list, club_list)


def add_win_percentage():  # EHHHH
    cluster = MongoClient(
        connection_string, tlsCAFile=certifi.where())  # MAC LINE
    db = cluster["Names_Cluster"]
    collection = db["Names"]

    for document in collection.find():
        win_per_list = (document.get("Pool_win_percentage"))
        # print(win_per_list)
        name = document.get("Name")
        win_per = round((sum(win_per_list) / len(win_per_list)), 2)
        # print(win_per)

        collection.update_one(
            {"Name": name}, {"$set": {"win_per_total": win_per}})

    return

# print(add_win_percentage())
