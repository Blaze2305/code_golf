### Code golf 2020
###### This is the repository for the backend compiler api and length judge for the Inspiro 2020 code golf event .

###### Run the code
```python
pip install -r requirements.txt 
python main.py 
```
You can then make requests to `localhost:5000`

###### API DOCS:
 * Use this for when they click on the test button, this will just test their code for their own input and will not be logged in the database 
      * /api/v1/test  methods == POST
		request format : JSON
		```	
            {
				'question_number':<question number 1-5,int >,
				'user_id':<user id >,
				'code':<source code , array of strings >,
				'inputs':<the input they give>
			}
		```
		response : JSON
		```
		if it compiles and works:
			    {
					'stdout':<the output captured,string>,
					'length':<the length of the code,int>
				}
		if it doesn't compile:
				{
					'stderr':<the error message capture>,
					'error':<the error code>
				}
		```
	
* Use this when they click on the submit button , this will run their code against our set of 
inputs and will log the total length in our database
	* /api/v1/submit     methods == POST
		```
        request format :  JSON
            {
		    	'question_number':<question number 1-5,int>,
			    'user_id':<user id>,
			    'code':<source code , array of strings>
	    	}

		response : JSON
			{
				'passed_all':<True or False depending on whether it passed all cases>
			}
		```