def add_new_class(class_links, class_name):
	class_links[class_name] = []

def add_links_to_class(class_links, class_name, link_names):
	while link_names.find(' ') != -1:
		name = link_names[0:link_names.find(' ')]
		link_names = link_names[link_names.find(' ') + 1:]
		class_links[class_name].append(name)
	name = link_names[0:]
	class_links[class_name].append(name)

def find_way(class_links, parent, child):
	if class_links.get(child) == None:
		return 'No'
	if class_links[child].count(parent) == 1:
		return 'Yes'
	else:
		for item in class_links[child]:
			# if item.empty():
				# continue
			answer = find_way(class_links, item, child)
			if answer:
				return answer
		return 'No'

number_of_classes = int(input())
class_links = dict()

for i in range(0, number_of_classes):
	inheritance = str(input())
	if inheritance.find(" : ") == -1:
		add_new_class(class_links, inheritance)
	else:
		class_name = inheritance[0:inheritance.find(" : ")]
		add_new_class(class_links, class_name)
		link_names = inheritance[inheritance.find(" : ") + 3:]
		add_links_to_class(class_links, class_name, link_names)

number_of_query = int(input())

for i in range(0, number_of_query):
	query = str(input())
	parent = query[0:query.find(' ')]
	child = query[query.find(' ') + 1:]
	answer = find_way(class_links, parent, child)
	print(answer)
