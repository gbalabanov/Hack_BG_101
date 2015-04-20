def revSum(number):
	return int(number)+int(str(number)[::-1])

def p_score(num):
	counter=1
	if counter==1:
		if str(num)[::-1]==str(num):
			score=1
		else:
			score=1
			counter+=1
			p_score(revSum(num))
	else:
			if str(num)[::-1]==str(num):
				score+=1
			else:
				score+=1
				p_score(revSum(num))
	return score
	

a=(input("Enter number:"))
print(p_score(a))

