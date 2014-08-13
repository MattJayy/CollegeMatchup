import json
from flask import Flask,request,render_template
 
app = Flask(__name__, static_url_path='')






def list_schools(gpa,sat=None):
	# open the json file to read only, 
	# read all context in the file stored into str_ variable 
	sat_ = 0
	if sat == None or sat == '' :
		sat_ = float(2400)
	else:
		sat_ = float(sat)	
	fo = open('school.json','r')
	schools_json = json.load(fo)
	fo.close()
	gpa_ = float(gpa)
	
	# made str_ into a json data type (list of dictionaries)
	new_list=[]
	for x in schools_json:
		if x['schoolType']=="Public"and x['gpa'] <= gpa_ and x['sat'] <= sat_:
			new_list.append(x)

		else:
			if x['gpa'] <= gpa_ and x['sat'] <= sat_ and x['schoolType']=="Private": 

			
				new_list.append(x)

	print "\t\tcount of schools with gpa <= %f is %d" %(gpa_, len(new_list))		
	return new_list	




		







@app.route('/contact', methods=['POST'])
def handle_contact_form():
	name = request.form['name_cf']
	mail = request.form['email_cf']
	message = request.form['message_cf']

	contact_dict = {'name':name,'mail': mail, 'message':message}
	contact_json = json.dumps(contact_dict)

	fo = open("contact_input.txt","a+")
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
	
	fo = open("support_input.txt","a+")
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

	print("\t\t\t %s ") % gpa_dict	
	fo = open("input.txt", "a+")
	
	fo.write(gpa_json)
	fo.write('\n')
	fo.close()		
	new_list = list_schools(gpa,sat)
	
	return render_template('template_table.html', schools=new_list)
	


@app.route('/signup', methods=['POST'])
def handle_Signup_form():
	fullname= request.form['name_sf']
	email= request.form['email_sf']
	month = request.form['month_sf']
	day = request.form['day_sf']
	year = request.form['year_sf']

	signup_dict ={'fullname':fullname,'email':email,'month':month,'day':day,'year':year}
	signup_json=json.dumps(signup_dict)
	
	fo = open("signup_input.txt", 'a+')
	fo.write(signup_json)
	fo.write('\n')
	fo.close()
	return signup_json



if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0') 
