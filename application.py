from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import redirect
import pymongo
from pymongo import MongoClient
import certifi
import json

from queryfunctions import query_results, comp_data, top_fencer_names
from mongo import connection_string


application = Flask(__name__)


@application.route('/', methods=["POST", "GET"])
def main():
    list_top_fencers = top_fencer_names()

    if request.method == "POST":  # IMPROVE SEARCH FUNCTION
        user = request.form["nm"]
        #user1 = request.form["nm1"]

        cluster = MongoClient(
            connection_string, tlsCAFile=certifi.where())  # MAC LINE
        db = cluster["Names_Cluster"]
        collection = db["Names"]
        cap_usr = user.upper()

        try:
            name_document = collection.find_one({"Name": cap_usr})
            # test to see if name is valid by querying win percentage
            win_pre = (name_document.get('Pool_win_percentage'))

            return redirect(url_for("user", usr=cap_usr))
        except:
            return render_template('index.html', topfencers=list_top_fencers)

    else:
        return render_template('index.html', topfencers=list_top_fencers)


# HOW TO CONTINUE URLS / / /
@application.route("/<usr>/", methods=["POST", "GET"])
def user(usr):
    results = query_results(usr, "all")
    message = "Alpha Version 1.914"
    # gprint(results[5])
    data = (results[5])  # Sending data to js functions for d3.js
    # results[5] is a list of dictionaries

    return render_template('profile.html', name=usr, results=results, message=message, data=data)


@application.route("/<usr>/y14", methods=["POST", "GET"])  # NO y14 DATA
def y14(usr):
    results = query_results(usr, "y14")
    message = "Alpha Version 1.914"
    return render_template('y14.html', name=usr, results=results, message=message)


@application.route("/<usr>/cadet", methods=["POST", "GET"])
def cadet(usr):
    results = query_results(usr, "cadet")
    message = "Alpha Version 1.914"
    return render_template('cadet.html', name=usr, results=results, message=message)


@application.route("/<usr>/junior", methods=["POST", "GET"])
def junior(usr):
    results = query_results(usr, "junior")
    message = "Alpha Version 1.914"
    return render_template('junior.html', name=usr, results=results, message=message)


@application.route("/<usr>/div1", methods=["POST", "GET"])
def div1(usr):
    results = query_results(usr, "div1")
    message = "Alpha Version 1.914"
    return render_template('div1.html', name=usr, results=results, message=message)


@application.route("/<usr>/div2", methods=["POST", "GET"])  # NO DIV2 DATA
def div2(usr):
    results = query_results(usr, "div2")
    message = "Alpha Version 1.914"
    return render_template('div2.html', name=usr, results=results, message=message)


@application.route("/<usr>/div3", methods=["POST", "GET"])  # NO DIV3 DATA
def div3(usr):
    results = query_results(usr, "div3")
    message = "Alpha Version 1.914"
    return render_template('div3.html', name=usr, results=results, message=message)


@application.route("/competition/<comp>", methods=["POST", "GET"])
def comp(comp):
    message = "Alpha Version 1.914"
    comp = comp_data(comp)
    # print(comp[0]) # TITLE
    # print(comp[1]) # Date
    # print(comp[2]) #COMP DATA
    return render_template('comp.html', title=comp[0], date=comp[1], data=comp[2], message=message)


@application.route("/competitions", methods=["POST", "GET"])
def comps():
    message = "Alpha Version 1.914"
    return render_template('comp_list.html', message=message)


@application.route("/fencers", methods=["POST", "GET"])
def fencers():
    message = "Alpha Version 1.914"
    return render_template('fencers_list.html', message=message)


@application.route("/betting", methods=["POST", "GET"])
def betting():
    message = "Alpha Version 1.914"
    return render_template('betting.html', message=message)


if __name__ == "__main__":
    application.run(debug=True)  # turn debug off for prodcution deployment
