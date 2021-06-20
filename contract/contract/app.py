#import json
#import mongocoll
from flask import Flask,jsonify, send_file, render_template
from flask.globals import request
from contract.API.db_connection import db
from flask_cors import CORS
from werkzeug.exceptions import BadRequest
from contract.utils import generate_fake_people
import json
app = Flask(__name__)
CORS(app)

data = []

for fp in generate_fake_people.people_generator(100):
    data.append(fp) 

data1 = json.dumps(data)
data2 = json.loads(data1)

app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

@app.route('/')
def hello():
	return render_template('Index.html')

@app.route('/Welcome')
def Welcome():
	return render_template('Welcome.html')

@app.route('/InvoiceAlert', methods = ['GET'])
def InvoiceAlert():
	return render_template('InvoiceAlert.html')

@app.route('/getInvoices', methods = ['GET'])
def getInvoices():
    return render_template('InvoiceAlert.html', data=data)

# @app.route('/checkInvoices', methods = ['POST'])
@app.route('/checkInvoices/<string:id>', methods = ['GET'])
def checkInvoices(id=None):
    for i in data:
        if i['id'] == id:
            return render_template('CheckInvoices.html', data=i)
    return []

@app.route('/runalgo', methods = ['POST'])
def runalgo():
    rd = request.form
    if rd:
        if int(rd['cibil'])>=750 and int(rd['KYCCheck'])==1:
            return jsonify({'response':'Eligible to Transfer full amount'}), 200
        else:
            return jsonify({'response':'No Amount can be transferred'}), 200


def main():
    app.run(host='0.0.0.0', port=5000,debug=True)

# if __name__ == '__main__':
#     main()
