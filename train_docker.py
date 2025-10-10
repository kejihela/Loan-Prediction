# Importing required packages
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from matplotlib import pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics


# Reading the data
data = pd.read_csv("prediction_model/dataset/train.csv")
num_col = data.select_dtypes(include=['int64','float64']).columns.tolist()
cat_col = data.select_dtypes(include=['object']).columns.tolist()
cat_col.remove('Loan_Status')
cat_col.remove('Loan_ID')
# Creating a list of categorical and numerical variables
for col in cat_col:
    data[col].fillna(data[col].mode()[0], inplace=True)

for col in num_col:
    data[col].fillna(data[col].median(), inplace=True)
# Clipping extreme values
data[num_col] = data[num_col].apply(lambda x: x.clip(*x.quantile([0.05, 0.95])))
# creating a new feature as Total Income
data['LoanAmount'] = np.log(data['LoanAmount']).copy()
data['TotalIncome'] = data['ApplicantIncome'] +data['CoapplicantIncome']
data['TotalIncome'] = np.log(data['TotalIncome']).copy()
# Dropping ApplicantIncome and CoapplicantIncome
data = data.drop(['ApplicantIncome','CoapplicantIncome'], axis=1)
for col in cat_col:
    le = preprocessing.LabelEncoder()
    data[col] = le.fit_transform(data[col])

data['Loan_Status'] = le.fit_transform(data['Loan_Status'])
# Train test split
X = data.drop(['Loan_Status', 'Loan_ID'], axis = 1)
y = data.Loan_Status

SEED = 1

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state = SEED)
#______________Logistic Regresssion__________________________#

lr = LogisticRegression(random_state=SEED)
lr_param_grid = {
'C': [100, 10, 1.0, 0.1, 0.01],
'penalty': ['l1','l2'],
'solver':['liblinear']
}

model = GridSearchCV(
estimator=lr,
param_grid=lr_param_grid,
cv=5,
n_jobs=-1,
scoring='accuracy',
verbose=0
)
model.fit(X_train, y_train)

# Menu driven

print("Type 'exit' to terminate.....\n")
print('''Gender: Female = 0, Male=1,
Married: No = 0, Yes = 1
Education: Graduate = 0 , Under-graduate = 1
Self_Employed: No = 0, Yes = 1,
Property_Area: Urban = 2, Semiurban = 1, Rural = 0,
Loan_Status: No = 0, Yes = 1\n''')

print('''Pass the data in following sequence separated by comma
 Gender, Married, Dependents,Education,Self_
loyed,LoanAmount,Loan_Amount_Term,Credit_History,Property_
a,TotalIncome\n''')

 # model = joblib.load('LR_model.pkl')

while True:
    user_data=input("Enter your data: ")

    if(user_data=="exit"):
        break

    data = list(map(float, user_data.split(',')))

    # exception handling
    if(len(data)<10):
        print("Incomplete data provided!!")
    else:

        # predicting the value
        predicted_value=model.predict([data])
        print("/_______________________________________________/")
        if (predicted_value[0]):
            print("\tCongratulations! your loan approval request is processed")
        else:
            print("\tSorry! your loan approval request is rejected")
            print("/_______________________________________________/")

