import json
from flask import Flask,request,render_template
app = Flask(__name__)






@app.route('/', methods=['POST'])
def Submit():
	request.form['name']
	request.form['email']
	request.form['message']
	return request.form['name']+request.form['email']+request.form['message']
	return render_template()
	










if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0') 
