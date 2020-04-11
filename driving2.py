#driving 2
country = input('你的國家是？ ')

if country == 'taiwan' :
	age = input('請輸入年齡？ ')
	age = int(age)
	if age >= 18 :
		print('你已經',age,'歲了，可以考駕照')
	else : 
		print('you`re not allowed to get liance!')
else :
	print('其他不知道！只知道台灣')
	
