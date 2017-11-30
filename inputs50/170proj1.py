def get_constraints(fname):
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
	return[num_constraints, num_people, constraints, list(s)]


def check_all(path, constraints):
	violates = 0
	for constraint in constraints:
		first = constraint[0]
		second = constraint[1]
		third = constraint[2]
		if first in path and second in path and third in path:
			firstIndex = path.index(first)
			secondIndex = path.index(second)
			thirdIndex = path.index(third)
			print(constraint)
			print(path)
			if (secondIndex < thirdIndex and thirdIndex < firstIndex) or (firstIndex < thirdIndex and thirdIndex < secondIndex):
				violates = 1
				break
	if violates == 0:
		return True
	else:
		return False



def done(fname):
	initial = get_constraints(fname)
	num_constraints = initial[0]
	num_people = initial[1]
	constraints = initial[2]
	people = initial[3]
	all_possible = []
	count = 2
	all_possible.append(people[0])
	all_possible.append(people[1])
	all_possible.append(people[2])
	blacklist = {}
	for i in range(0, num_people):
		blacklist[i] = []
	while(count != num_people):
		if(check_all(all_possible, constraints) == True):
			for p in people:
				if(p not in all_possible && !blacklist[count].contains(p)):
					all_possible.append(p)
					count+=1
		else:
			blacklist[count].append(all_possible[count])
			all_possible.remove(count)
			for p in people:
				if(p not in all_possible && !blacklist[count].contains(p)):
					all_possible.append(p)
			if len(blacklist[count]) == num_people:
				blacklist[count] = []
				count -= 1
				blacklist[count].append(all_possible[count])
				all_possible.remove(count)
