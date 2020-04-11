#driving 1
country = input('你的國家是？ ')
age = input('請輸入年齡？ ')
age = int(age)
if country == 'taiwan' :
	if age >= 18 :
		print('你已經',age,'歲了，可以考駕照')
	else : 
		print('you`re not allowed to get liance!')


