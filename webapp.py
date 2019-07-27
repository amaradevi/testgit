from flask import Flask,jsonify,request,json
import os,sys
import time
app = Flask(__name__)

employees = [{"id":1,"fname":"Amara","lname":"Devi","Dep":"OMC"},
	{"id":2,"fname":"Kamal","lname":"Singh","Dep":"OMC"}
]
###this is for tetsing
###this is for testing1
##this is for remote branch creation
@app.route("/",methods=['GET'])
def get_employees():
	return jsonify(employees)

@app.route("/",methods=['POST'])
def create_employee():
	employee={"id":employees[-1]["id"]+1,"fname":request.json["fname"],"lname":request.json["lname"],"Dep":request.json["dep"]}
	employees.append(employee)
	return jsonify({"json created":employee}), 201

@app.route("/employee/<int:empnum>",methods=['GET'])
def get_employee(empnum):
		
	employee=[e for e in employees if e["id"]==empnum]
	if len(employee) == 0:
		return jsonify({"Employee not exists":empnum}), 404
	return jsonify(employee)
	
@app.route("/employee/<int:empnum>",methods=['DELETE'])
def delete_employee(empnum):
		
	employee=[e for e in employees if e["id"]==empnum]
	if len(employee) == 0:
		return jsonify({"Employee not exists":empnum}), 404
	employees.remove(employee[0])
	return jsonify({"employee deleted":empnum}), 204
		

	
	
if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')
	
	
