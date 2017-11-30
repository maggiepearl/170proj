from constraint import *
import random

def check_all(path, constraints):
	violates = 0
	inConflict = []
	inConflictIndex = set()
	failed_constraints =  []
	for constraint in constraints:
		first = constraint[0]
		second = constraint[1]
		third = constraint[2]
		if first in path and second in path and third in path:
			firstIndex = path.index(first)
			secondIndex = path.index(second)
			thirdIndex = path.index(third)

			if (secondIndex < thirdIndex and thirdIndex < firstIndex) or (firstIndex < thirdIndex and thirdIndex < secondIndex):
				violates +=1
				inConflict.append(third)
				inConflictIndex.add(path.index(third))
				# inConflict.add(second)
				# inConflictIndex.add(path.index(second))
				# inConflict.add(first)
				# inConflictIndex.add(path.index(first))
				failed_constraints.append(constraint)
	return violates, inConflict, failed_constraints

def check_all3(path, constraints):
	violates = 0
	inConflict = []
	inConflictIndex = set()
	failed_constraints =  []
	for constraint in constraints:
		first = constraint[0]
		second = constraint[1]
		third = constraint[2]
		if first in path and second in path and third in path:
			firstIndex = path.index(first)
			secondIndex = path.index(second)
			thirdIndex = path.index(third)

			if (secondIndex < thirdIndex and thirdIndex < firstIndex) or (firstIndex < thirdIndex and thirdIndex < secondIndex):
				violates +=1
				inConflict.append(third)
				inConflictIndex.add(path.index(third))
				# inConflict.add(second)
				# inConflictIndex.add(path.index(second))
				# inConflict.add(first)
				# inConflictIndex.add(path.index(first))
				failed_constraints.append(constraint)
	return violates

def check_all2(path, constraints):
	violates = 0
	inConflict = []
	inConflictIndex = set()
	failed_constraints =  []
	for constraint in constraints:
		first = constraint[0]
		second = constraint[1]
		third = constraint[2]
		if first in path and second in path and third in path:
			firstIndex = path.index(first)
			secondIndex = path.index(second)
			thirdIndex = path.index(third)

			if (secondIndex < thirdIndex and thirdIndex < firstIndex) or (firstIndex < thirdIndex and thirdIndex < secondIndex):
				violates +=1
				inConflict.append(third)
				inConflictIndex.add(path.index(third))
				inConflict.append(second)
				inConflictIndex.add(path.index(second))
				inConflict.append(first)
				inConflictIndex.add(path.index(first))
				failed_constraints.append(constraint)
	return violates, inConflict, failed_constraints

def margaret(optimal, constraints):
	for i in range(1, len(optimal)):
		prev = check_all3(optimal, constraints)
		temp = optimal[:]
		temp[i], temp[i-1] = temp[i-1], temp[i]
		violates = check_all3(temp, constraints)
		if violates < prev:
			optimal = temp
			print("hey")
	return optimal

def dianarox(fname):
	with open(fname) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	num_constraints = int(content[1])
	num_people = int(content[0])
	content = content[2:]
	constraints = []
	s = set()
	for elem in content:
		t = elem.split()
		constraints.append(t)
		for x in t:
			s.add(x)
	variables = []
	domains = []
	people = list(s)
	for i in range(num_people):
		domains.append(i)
	optimal = list(s)
	violates = num_constraints
	checked = set()
	again = 0
	again2 = violates
	tried = set()
	while violates != 0:
		violates, inConflict, x = check_all(optimal, constraints)
		if(violates < 10):
			print(optimal)
		if (violates > 0):
			tried.add(tuple(optimal))

		else:
			return optimal
		if (again2 == violates):
			again+=1
		else:
			again = 0


		if(again == 10):
			again = 0
			random.shuffle(optimal)
			violates, inConflict, x = check_all(optimal, constraints)
			test = tuple(optimal)
			if (test in tried):
				while(test in tried):
					random.shuffle(optimal)
					test = tuple(optimal)
			tried.add(test)
			violates, inConflict, x = check_all(optimal, constraints)
		again2 = violates
		print(violates)
		new_in_conflict = inConflict
		for element in inConflict:
			if element not in new_in_conflict:
				element = random.sample(new_in_conflict,1)[0]
			best = optimal
			best_num = 1000
			index = best.index(element)
			for i in range(len(optimal)):
				if (optimal[i] == element):
					continue
				temp = best[:]
				temp[i], temp[index] = temp[index], temp[i]
				tester = tuple(temp)
				if (tester in tried):
					continue
				violates_temp, inConflicttemp, x = check_all(temp, constraints)
				if violates_temp <= violates:
					best = temp[:]
					best_num = violates_temp
					new_in_conflict = inConflicttemp
					if (best_num) == 0:
						return best
					tried.add(tuple(best))
			if best_num <= violates:
				optimal = best[:]
				violates = best_num
	ret = ""
	for person in optimal:
		ret = ret + person + " "
	print(ret)
	return optimal




