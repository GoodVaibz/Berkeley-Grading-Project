import csv 

def create_csv(orderedDicts, filename):
	csv_output = open(filename, 'wb')
	wr = csv.writer(csv_output, quoting=csv.QUOTE_NONNUMERIC)
	for classname in orderedDicts[0].keys():
		new_row = []
		new_row.append(classname)
		new_row.append(classname.split(' ')[0])
		for i in range(len(orderedDicts)):
			new_row.append(orderedDicts[i][classname])
		wr.writerow(new_row)
