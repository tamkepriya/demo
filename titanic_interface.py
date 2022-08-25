
from flask import Flask,jsonify,redirect,request,render_template
import config
from titanicsutils import Titanic_Classification
app=Flask(__name__)
#######################################################################
##########################Titanic Classification API##########################
#######################################################################

@app.route("/")
def abc():
    return render_template("index.html")


@app.route("/titanic_prediction",methods=["POST","GET"])
def titanic_prediction():

    data=request.form
    Pclass=eval(data["Pclass"])
    Age=eval(data["Age"])
    SibSp=eval(data["SibSp"])
    Parch=eval(data["Parch"])
    Fare=eval(data["Fare"])
    Gender=str(data["Gender"])
    Embarked=str(data["Embarked"])
    print("DAta=====",data)

    obj=Titanic_Classification()
    result=obj.get_predicted_class(Pclass, Age, SibSp, Parch ,Fare ,Gender ,Embarked)

    # return jsonify({"Predicted class is-^_^-==":f"{result}"})

    return render_template("after.html",data=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)


# {% if result %}
#         <p>{{ result }}</p>
#     {% endif %}