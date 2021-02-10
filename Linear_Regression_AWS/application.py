# Importing Necessary Libraries
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

# Initializing a flask app
application = Flask(__name__)

# When first time application is called it will render to index.html page
@application.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

# When Post Method is initiated it will call index function
# Index function will save data provided my user in variables


@application.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if (is_research == 'yes'):
                research = 1
            else:
                research = 0
            filename = 'finalized_model.pickle'
            # loading the model file
            loaded_model = pickle.load(open(filename, 'rb'))
            # prediction using loaded model
            prediction = loaded_model.predict([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
            print('Prediction is ', prediction)
            # showing the prediction results in a UI
            return render_template('result.html', prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is : ', e)
            return 'Something is Wrong '

    else:
        return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)
