from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import redirect
import pymongo 
from pymongo import MongoClient
import certifi

from queryfunctions import query_results


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
            win_pre = (name_document.get('Pool_win_percentage') ) #test to see if name is valid by querying win percentage
            
            return redirect(url_for("user", usr=cap_usr))
        except:
            flash_message="True"
            return render_template('index.html', flash_message=flash_message)

    else:
        flash_message="True"
        return render_template('index.html', flash_message=flash_message)



@application.route("/<usr>/", methods=["POST","GET"]) #HOW TO CONTINUE URLS / / /
def user(usr):
    results = query_results(usr, "all")
    message = "Alpha Version 1.914"
    return render_template('profile.html', name=usr, results=results, message=message)
                            
@application.route("/<usr>/y14", methods=["POST","GET"]) #NO y14 DATA
def y14(usr):
    results = query_results(usr, "y14")
    message = "Alpha Version 1.914"
    return render_template('y14.html', name=usr, results=results, message=message)

@application.route("/<usr>/cadet", methods=["POST","GET"])
def cadet(usr):
    results = query_results(usr, "cadet")
    message = "Alpha Version 1.914"
    return render_template('cadet.html', name=usr, results=results, message=message)

@application.route("/<usr>/junior", methods=["POST","GET"])
def junior(usr):
    results = query_results(usr, "junior")
    message = "Alpha Version 1.914"
    return render_template('junior.html', name=usr, results=results, message=message)

@application.route("/<usr>/div1", methods=["POST","GET"])
def div1(usr):
    results = query_results(usr, "div1")
    message = "Alpha Version 1.914"
    return render_template('div1.html', name=usr, results=results, message=message)

@application.route("/<usr>/div2", methods=["POST","GET"])   #NO DIV2 DATA
def div2(usr):
    results = query_results(usr, "div2")
    message = "Alpha Version 1.914"
    return render_template('div2.html', name=usr, results=results, message=message)

@application.route("/<usr>/div3", methods=["POST","GET"])   #NO DIV3 DATA
def div3(usr):
    results = query_results(usr, "div3")
    message = "Alpha Version 1.914"
    return render_template('div3.html', name=usr, results=results, message=message)


if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment
