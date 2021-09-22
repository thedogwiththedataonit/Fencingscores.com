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
            return render_template('index.html', error="No Name")

    else:
        return render_template('index.html')



@application.route("/<usr>/allcompetitions", methods=["POST","GET"]) #HOW TO CONTINUE URLS / / /
def user(usr):
    results = query_results(usr, "all")
    return render_template('profile.html', name=usr, results=results)
                            
@application.route("/<usr>/y14", methods=["POST","GET"]) #NO y14 DATA
def y14(usr):
    results = query_results(usr, "y14")
    return render_template('y14.html', name=usr, results=results)

@application.route("/<usr>/cadet", methods=["POST","GET"])
def cadet(usr):
    results = query_results(usr, "cadet")
    return render_template('cadet.html', name=usr, results=results)

@application.route("/<usr>/junior", methods=["POST","GET"])
def junior(usr):
    results = query_results(usr, "junior")
    return render_template('junior.html', name=usr, results=results)

@application.route("/<usr>/div1", methods=["POST","GET"])
def div1(usr):
    results = query_results(usr, "div1")
    return render_template('div1.html', name=usr, results=results)

@application.route("/<usr>/div2", methods=["POST","GET"])   #NO DIV2 DATA
def div2(usr):
    results = query_results(usr, "div2")
    return render_template('div2.html', name=usr, results=results)

@application.route("/<usr>/div3", methods=["POST","GET"])   #NO DIV3 DATA
def div3(usr):
    results = query_results(usr, "div3")
    return render_template('div3.html', name=usr, results=results)


if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment
