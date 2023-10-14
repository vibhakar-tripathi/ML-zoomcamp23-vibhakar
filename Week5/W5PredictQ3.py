
import pickle

from sklearn import model_selection
from sklearn import feature_extraction
from sklearn.linear_model import LogisticRegression

input_model_file = 'model1.bin'
input_dv_file = 'dv.bin'

f_model = open(input_model_file,'rb')
f_dv = open(input_dv_file,'rb')

model = pickle.load(f_model)
dv = pickle.load(f_dv)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

x= dv.transform([client])
y_pred = model.predict_proba(x)[0,1]

print("prediction:",y_pred)

