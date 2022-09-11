
import numpy as np
import json
import pickle
import config

class Diabetes_Classification():
    # def __init__ (Glucose, BloodPressure, SkinThickness, Insulin ,BMI ,DiabetesPedigreeFunction ,Age):
    #     self.Glucose=Glucose
    #     self.BloodPressure=BloodPressure
    #     self.SkinThickness=SkinThickness
    #     self.Insulin=Insulin
    #     self.BMI=BMI
    #     self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
    #     self.Age=Age
    #     return
    def model_file(self):
        with open("rf_model4_10.pkl","rb") as f:
            self.rf_model4_10=pickle.load(f)
        with open("project_data.json", "r") as f:
            self.project_data = json.load(f)
        return
    def get_predicted_class(self,Glucose, BloodPressure, SkinThickness, Insulin ,BMI ,DiabetesPedigreeFunction ,Age):
        self.model_file()
        column_list = self.project_data.get("columns")

        input_array = np.zeros(len(column_list))
        print('column_list :::::-',column_list)
        
        input_array[0] = Glucose
        input_array[1] = BloodPressure
        input_array[2] = SkinThickness
        input_array[3] = Insulin
        input_array[4] = BMI
        input_array[5] = DiabetesPedigreeFunction
        input_array[6] = Age
    
        predicted_class=self.rf_model4_10.predict([input_array])[0]
        classes={0:"yes",
                1:"no"}
        prediction=classes[predicted_class]
        print("class is=",prediction)
        return prediction
if __name__=="__main__":
    obj=Diabetes_Classification()
    result=obj.get_predicted_class(Glucose, BloodPressure, SkinThickness, Insulin ,BMI ,DiabetesPedigreeFunction ,Age)
    print("predicted classs is====",result)

