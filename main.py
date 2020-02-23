from firebase_admin import firestore, credentials
import firebase_admin
from flask import Flask,jsonify,request
from requests import post
from json import loads
import test_cases

token = '60d62a9c-de2a-4efa-b0dc-45f5c13f4459'
headers={"Authorization":f"Token {token}","Content-type":"application/json"}
url='https://run.glot.io/languages/c/latest'

# Firebase init
cred = credentials.Certificate("code_golf.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
users_collection = db.collection('users')

app = Flask(__name__)
@app.route('/api/v1/test',methods=['POST'])
def compile_code():
	if(request.method=='POST'):
		source = request.get_json()
		number = source['question_number']
		uid = source['user_id']
		code = '\n'.join(source['code'])
		inputs = source['inputs']
		filename = str(uid)+str(number)+'.c'
		data = {'files':[{'name':filename,'content':code}],'stdin':inputs}
		req = loads(post(url,data=str(data),headers=headers).text)
		app.logger.info(f'{req},\n\n\nherere')
		if(req['error']):
			back = {'stderr':req['stderr'],'error':req['error']}
		else:
			file = minify(code)
			back = {'stdout':req['stdout'],'length':len(file)}
			app.logger.info(file)

		return jsonify(back)

@app.route('/api/v1/submit',methods=["POST"])
def submit_code():
	source = request.get_json()
	number = int(source['question_number'])
	code = '\n'.join(source['code'])
	uid = source['user_id']
	input_cases = test_cases.tests[number]['test_input']
	output_cases = test_cases.tests[number]['test_output']
	flag = True

	for i in range(0,3):
		if(flag):
			inputs = input_cases[i]
			filename = str(uid)+str(number)+'.c'
			data = {'files':[{'name':filename,'content':code,'stdin':inputs}]}
			req = loads(post(url,data=str(data),headers=headers).text)
			if(req['error']):
				flag = False
				break
			elif(req['stdout']!=output_cases[i]):
				flag = False
				break
	if(flag):
		file = minify(code)
		data = {'question_number':number,'code':source['code'],'length':len(file)}
		users_collection.document(f'{source["user_id"]}').set(data)

	return(jsonify({'passed_all':flag}))


def minify(code):
	file = code.replace("\\n",'\n')
	file = file.replace('\t','')
	file = file.replace(' ','')
	file = file.replace('\n','')
	return(file)
	
app.run(host='0.0.0.0',port='5000',debug=True)

