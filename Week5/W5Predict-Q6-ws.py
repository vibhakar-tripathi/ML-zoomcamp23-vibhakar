
import pickle

from sklearn import model_selection
from sklearn import feature_extraction
from sklearn.linear_model import LogisticRegression


from flask import Flask
from flask import request
from flask import jsonify

input_model_file = 'model2.bin'
input_dv_file = 'dv.bin'

app = Flask('credit')
f_model = open(input_model_file,'rb')
f_dv = open(input_dv_file,'rb')

model = pickle.load(f_model)
dv = pickle.load(f_dv)
#client = {"job": "retired", "duration": 445, "poutcome": "success"}

@app.route('/predict',methods=['POST'])

def predict():
    client=request.get_json()

    x= dv.transform([client])
    y_pred = model.predict_proba(x)[0,1]

    result=("credit probability:", y_pred)
    print ("WS-credit-result:",y_pred)

    return (jsonify(result))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9670)


