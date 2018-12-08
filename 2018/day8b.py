text = list(map(lambda x: int(x), [x.strip() for x in open('day8input.txt', 'r')][0].split()))
#text = list(map(lambda x: int(x), [x.strip() for x in open('day8test.txt', 'r')][0].split()))

def generate_node(s):
	#print(s)
	child_node_count = s[0]
	metadata_entries_count = s[1]
	metadata_sum = 0
	value = 0
	length = 2
	s = s[2:]
	child_values = {}
	for k in range(child_node_count):
		child_length, child_metadata_sum, child_values[k+1] = generate_node(s)
		s = s[child_length:]
		metadata_sum += child_metadata_sum
		length += child_length
	
	length += metadata_entries_count
	metadata_sum += sum(s[:metadata_entries_count])
	if child_node_count == 0:
		value = metadata_sum
	else:
		for i in s[:metadata_entries_count]:
			if i in child_values:
				value += child_values[i]
	print(value)
	return length, metadata_sum, value

	

print(generate_node(text))