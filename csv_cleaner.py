import csv
import sys
out_file = sys.argv[1][:-4] + '_clean.csv'
csvwriter = csv.writer(open(out_file,'wb'))
with open(sys.argv[1], 'rU') as csvfile:
	csvreader = list(csv.reader(csvfile))
	for row in csvreader[1:]:
		new_row = list(row)
		new_row[1] = new_row[1].strip(' ')
		while new_row[1][0] == '0':
			new_row[1] = new_row[1][1:]
		if "R0" in new_row[1]:
			new_row[1] = new_row[1][0] + new_row[1][3:]


		csvwriter.writerow(new_row)
out_file.close()
csvfile.close()