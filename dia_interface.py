
from flask import Flask,jsonify,redirect,request,render_template
import config
from diabetessutils import Diabetes_Classification
app=Flask(__name__)
#######################################################################
##########################Diabetes Classification API##########################
#######################################################################

@app.route("/")
def abc():
    return render_template("index.html")


@app.route("/diabetes_prediction",methods=["POST","GET"])
def diabetes_prediction():

    data=request.form
    Glucose=eval(data["Glucose"])
    BloodPressure=eval(data["BloodPressure"])
    SkinThickness=eval(data["SkinThickness"])
    Insulin=eval(data["Insulin"])
    BMI=eval(data["BMI"])
    DiabetesPedigreeFunction=eval(data["DiabetesPedigreeFunction"])
    Age=eval(data["Age"])
    print("DAta=====",data)

    obj=Diabetes_Classification()
    result=obj.get_predicted_class(Glucose, BloodPressure, SkinThickness, Insulin ,BMI ,DiabetesPedigreeFunction ,Age)

    # return jsonify({"Predicted class is-^_^-==":f"{result}"})

    return render_template("after.html",data=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)


# {% if result %}
#         <p>{{ result }}</p>
#     {% endif %}