def __init__dict(parent_namespace):
	Dict = dict()
	Dict['parent_namespace'] = parent_namespace
	Dict['variables'] = []
	return (Dict)

def print_output(Namesp, namespace, arg):
	if namespace == 'None':
		print('None')
		return (1)
	if arg in Namesp[namespace]['variables']:
		print(namespace)
		return (1)
	return (print_output(Namesp, Namesp[namespace]['parent_namespace'], arg))

def query_processing(Namesp, query, namespace, arg):
	if query == "add":
		Namesp[namespace]['variables'].append(arg)
	elif query == "create":
		Namesp[namespace] = __init__dict(arg)
	elif query == "get":
		print_output(Namesp, namespace, arg)

n = int(input())
Namesp = dict()
Namesp['global'] = __init__dict('None')

for i in range(0, n):
	query, namespace, arg = input().split(' ')
	query_processing(Namesp, query, namespace, arg)
