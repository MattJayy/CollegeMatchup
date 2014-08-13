import json 

def list_schools(gpa):
	# open the json file to read only, 
	# read all context in the file stored into str_ variable 
	fo = open('school.json','r')
	schools_json = json.load(fo)
	fo.close()

	# made str_ into a json data type (list of dictionaries)
	new_list=[]
	for x in schools_json:
		if x['gpa'] <= gpa:
			new_list.append(x)
	return new_list		


	
		

	

new = list_schools(2.5)
print new 


	# print "Read string is :", str_
	# print type(str_)

	

	

	# print type(schools_json)
	