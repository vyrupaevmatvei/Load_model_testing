import pickle
import json
import pandas as pd

# Creating class to define the request body
# and the type hints of each attribute
class request_body():
    PassengerId : str
    Pclass : str
    Name : str
    Sex : str
    Age : str
    SibSp : str
    Parch : str
    Ticket : str
    Fare : str
    Cabin : str
    Embarked : str

model = None
with open('models/model.pkl', 'rb') as fd:
    model = pickle.load(fd)

def processed_input_data(data_body):
    Sex_female = 0
    Sex_male = 0
    Embarked_C = 0
    Embarked_Q = 0
    Embarked_S = 0

    if data_body.Sex == "male":
        Sex_male = 1
    if data_body.Sex == "female":
        Sex_female = 1
    if data_body.Embarked == "C":
        Embarked_C = 1
    if data_body.Embarked == "Q":
        Embarked_Q = 1
    if data_body.Embarked == "S":
        Embarked_S = 1

    x = pd.DataFrame(data = {
        'Pclass': [int(data_body.Pclass)],
        'SibSp': [int(data_body.SibSp)],
        'Parch': [int(data_body.Parch)],
        'Fare': [float(data_body.Fare)],
        'Age': [float(data_body.Age)],
        'Sex_female': [Sex_female],
        'Sex_male': [Sex_male],
        'Embarked_C': [Embarked_C],
        'Embarked_Q': [Embarked_Q],
        'Embarked_S': [Embarked_S]
    })
    return x


if __name__ == "__main__":
    test_data = request_body()
    test_data.PassengerId = "601"
    test_data.Pclass = "2"
    test_data.Name = "Jacobsohn, Mrs. Sidney Samuel (Amy Frances Christy)"
    test_data.Sex = "female"
    test_data.Age = "24"
    test_data.SibSp = "2"
    test_data.Parch = "1"
    test_data.Ticket = "243847"
    test_data.Fare = "27"
    test_data.Cabin = ""
    test_data.Embarked = "S"

    x = processed_input_data(test_data)
    predicted_qualities = model.predict(x)
    print(predicted_qualities)
