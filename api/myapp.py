import json
from flask import Flask,request,render_template
app = Flask(__name__)



@app.route('/')
def test_server():
	return "helloworld"


@app.route('/contact', methods=['POST'])
def handle_contact_form():
	name = request.form['name_cf']
	mail = request.form['email_cf']
	message = request.form['message_cf']

	contact_dict = {'name':name,'mail': mail, 'message':message}
	contact_json = json.dumps(contact_dict)
	return contact_json













if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0') 
