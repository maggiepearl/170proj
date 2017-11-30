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
	names = dict.fromkeys(s,0)
	for constraint in constraints:
		third = constraint[2]
		names[third] += 1
	retnames = sorted(names, key=names.get, reverse=True)
	return[num_constraints, num_people, constraints, retnames]


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
		namesordered = []
		for i in range(0, len(all_possible)):
			if (i%2 == 0):
				ind = 0
			else:
				ind = 1
			if ind == 0:
				namesordered = [all_possible[i]] + namesordered
			else:
				namesordered.append(all_possible[i])
		if(check_all(namesordered, constraints) == True):
			count+=1
			if(count == num_people):
				return namesordered
			for p in people:
				if(p not in all_possible):
					all_possible.append(p)
					blacklist[count].append(all_possible[count])
					people = people[1:] + people[0:1]
					break
		else:
			while(len(blacklist[count]) == num_people-count):
				blacklist[count] = []
				all_possible = all_possible[:len(all_possible)-1]
				people = people[len(people)-1:len(people)] + people[0:len(people)-1]
				count -= 1
			for p in people:
				if(p not in all_possible and p not in blacklist[count]):
					all_possible[count] = p
					blacklist[count].append(all_possible[count])
					break
	return all_possible
