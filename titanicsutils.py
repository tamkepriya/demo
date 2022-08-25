
import numpy as np
import json
import pickle
import config

class Titanic_Classification():
    # def __init__ (self,Pclass,Age,SibSp,Parch,Fare,Gender,Embarked):
    #     self.Pclass=Pclass
    #     self.Age=Age
    #     self.SibSp=SibSp
    #     self.Parch=Parch
    #     self.SibSp=SibSp
    #     self.Fare=Fare
    #     self.Gender=Gender
    #     self.Embarked=Embarked
    #     return
    def model_file(self):
        with open("Titanic_model.pkl","rb") as f:
            self.titanic_model=pickle.load(f)
        with open("titanic_columns.json", "r") as f:
            self.data_columns = json.load(f)
        return
    def get_predicted_class(self,Pclass,Age,SibSp,Parch,Fare,Gender,Embarked):
        self.model_file()
        column_list = self.data_columns.get("columns")

        input_array = np.zeros(len(column_list))
        print('column_list :::::-',column_list)
        gender_index = column_list.index(Gender)
        embaked_index = column_list.index(Embarked)
        input_array[0] = Pclass
        input_array[1] = Age
        input_array[2] =SibSp
        input_array[3] = Parch
        input_array[4] = Fare
        input_array[gender_index] = 1
        input_array[embaked_index] = 1
    
        predicted_class=self.titanic_model.predict([input_array])[0]
        classes={0:"Dead",
                1:"Live"}
        prediction=classes[predicted_class]
        print("class is=",prediction)
        return prediction
if __name__=="__main__":
    obj=Titanic_Classification()
    #result=obj.get_predicted_class(Pclass,Age,SibSp,Parch,Fare,Gender,Embarked)
    result=obj.get_predicted_class(2,25,3,5,2,'female','S')
    print("predicted classs is====",result)

