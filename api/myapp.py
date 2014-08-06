import json
from flask import Flask,request
app = Flask(__name__)





@app.route('/contact', methods=['POST'])
def handle_contact_form():
	name = request.form['name_cf']
	mail = request.form['email_cf']
	message = request.form['message_cf']

	contact_dict = {'name':name,'mail': mail, 'message':message}
	contact_json = json.dumps(contact_dict)

	fo = open("input.txt","a+")
	fo.write(contact_json)
	fo.write('\n')
	fo.close()
	return contact_json

@app.route('/support',methods =['POST'])
def handle_support_form():
	reccomand = request.form['reccomand_sf']
	problem = request.form['problem_sf']
	change = request.form['change_sf']

	support_dict = {'recommand':reccomand,'problem': problem, 'change':change}
	support_json =json.dumps(support_dict)
	
	fo = open("input.txt","a+")
	fo.write(support_json)
	fo.write('\n')
	fo.close()
	return support_json

@app.route('/GPA', methods=['POST'])
def handle_gpa_form():
	gpa = request.form['gpa_gf']
	sat = request.form['sat_gf']
	school_type = request.form['type_gf']
	size = request.form['size_gf']

	gpa_dict = {'gpa': gpa,'sat': sat, 'type': school_type,'size': size}
	#gpa_dict = {'gpa': gpa,'sat': sat}
	gpa_json=json.dumps(gpa_dict)
	
	fo = open("input.txt", "a+")
	
	fo.write(gpa_json)
	fo.write('\n')
	fo.close()
	return gpa_json




@app.route('/signup', methods=['POST'])
def handle_Signup_form():
	fullname= request.form['name_sf']
	email= request.form['email_sf']
	month = request.form['month_sf']
	day = request.form['day_sf']
	year = request.form['year_sf']

	signup_dict ={'fullname':fullname,'email':email,'month':month,'day':day,'year':year}
	signup_json=json.dumps(signup_dict)
	
	fo = open("input.txt", 'a+')
	fo.write(signup_json)
	fo.write('\n')
	fo.close()
	return signup_json









	




if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0') 
