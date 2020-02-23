tests={
	1:{
		'test_input':['john','man','woman'],
		'test_output':['Ravenclaw','Gryffindor','Hufflepuff']
	},

	2:{
		'test_input':['NISB','thisisastring','helloworld'],
		'test_output':['N__B','t__s_s_str_n_','h__l_w_rld']
	},

	3:{
		'test_input':['24','123','198'],
		'test_output':['6','6','9']
	},

	4:{
		'test_input':['5','7','3'],
		'test_output':['''   *    \n  ***   \n *****  ''',
					'''    *     \n   ***    \n  *****   \n *******  ''',
					'''  *  \n *** ''']
	},

	5:{
		'test_input':['5\n5 4 2 7 9','6\n9 8 0 1 3 2','7\n5 4 3 2 1 6 8'],
		'test_output':['2 4 5 7 9','0 1 2 3 8 9','1 2 3 4 5 6 8']
	}
}