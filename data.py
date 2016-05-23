import csv

year1 = 2007
year2 = 2015

spring_file2007 = 'spring_' + str(year1) + '_clean.csv'
spring_file2015 = 'spring_' + str(year2) + '.csv'
fall_file2007 = 'fall_' + str(year1) + '_clean.csv'
fall_file2015 = 'fall_' + str(year2) + '.csv'
open_spring_file2007 = open(spring_file2007, 'rU')
open_spring_file2015 = open(spring_file2015, 'rU')
open_fall_file2007 = open(fall_file2007, 'rU')
open_fall_file2015 = open(fall_file2015, 'rU')

def get_matching_classes(file_2007, file_2015):
	matching_class = set()
	csvreader2007 = list(csv.reader(file_2007))
	csvreader2015 = list(csv.reader(file_2015))
	for row_07 in csvreader2007[1:]:
		row_07 = list(row_07)
		row_07_class = row_07[0] + ' ' + row_07[1].strip(' ')
		
		for row_15 in csvreader2015[1:]:


			row_15 = list(row_15)
			row_15_class = row_15[2] + ' ' + row_15[4]
			if row_07_class == row_15_class:
				matching_class.add(row_15_class)
	return matching_class

def get_grade_tuple(filename, className, year):
	num_A = 0
	num_A_minus = 0
	num_A_plus = 0
	num_B = 0
	num_B_minus = 0
	num_B_plus = 0
	num_C = 0
	num_C_minus = 0
	num_C_plus = 0
	num_D = 0
	num_D_minus = 0
	num_D_plus = 0
	num_F = 0
	abbrev = className.split(' ')[0]
	class_num = className.split(' ')[1]
	csvreader = list(csv.reader(filename))
	if year == 2007:	
		print csvreader
		for row in csvreader[1:]:
			row = list(row)
			if abbrev == row[0] and class_num == str(row[1]):
				num_A_plus += row[5]
				num_A += row[6]
				num_A_minus += row[7]
				num_B_plus += row[8]
				num_B += row[9]
				num_B_minus += row[10]
				num_C_plus += row[11]
				num_C += row[12]
				num_C_minus += row[13]
				num_D_plus += row[14]
				num_D += row[15]
				num_D_minus += row[16]
				num_F += row[17]
				print num_F			
	elif year == 2015:
		for row in csvreader[1:]:
			row = list(row)
			if abbrev == row[1] and class_num == str(row[3]):
				 if row[9] != '':
					num_A_plus += row[9]
				 if row[10] != '':
					num_A += row[10]
				 if row[11] != '':
					num_A_minus += row[11]
				 if row[12] != '':
					num_B_plus += row[12]
				 if row[13] != '':
					num_B += row[13]
				 if row[14] != '':
					num_B_minus += row[14]
				 if row[15] != '':
					num_C_plus += row[15]
				 if row[16] != '':
					num_C += row[16]
				 if row[17] != '':
					num_C_minus += row[17]	
				 if row[18] != '':
					num_D_plus += row[18]
				 if row[19] != '':
					num_D += row[19]
				 if row[20] != '':
					num_D_minus += row[20]		
				 if row[21] != '':
					num_D += row[21]

	grade_list = (num_A_plus, num_A, num_A_minus, num_B_plus, num_B, num_B_minus, num_C_plus, num_C, num_C_minus, num_D_plus, num_D, num_D_minus, num_F)
	return grade_list


fall_matching_classes = get_matching_classes(open_fall_file2007, open_fall_file2015)
spring_matching_classes = get_matching_classes(open_spring_file2007, open_spring_file2015)
fall_grade_dict = {}
spring_grade_dict = {}
for f_matching_class in fall_matching_classes:
	f_grade_2015 = get_grade_tuple(open_fall_file2015, f_matching_class, 2015)
	f_grade_2007 = get_grade_tuple(open_fall_file2007, f_matching_class, 2007)
	fall_grade_dict[f_matching_class] = (f_grade_2007, f_grade_2015)

for s_matching_class in spring_matching_classes:
	s_grade_2007 = get_grade_tuple(open_spring_file2007, s_matching_class, 2007)
	s_grade_2015 = get_grade_tuple(open_spring_file2015, s_matching_class, 2015)
	spring_grade_dict[s_matching_class] = (s_grade_2007, s_grade_2015)

