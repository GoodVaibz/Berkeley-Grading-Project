import csv
from collections import OrderedDict
from itertools import islice


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
s_csvreader2007 = list(csv.reader(open_spring_file2007))
s_csvreader2015 = list(csv.reader(open_spring_file2015))
f_csvreader2007 = list(csv.reader(open_fall_file2007))
f_csvreader2015 = list(csv.reader(open_fall_file2015))

def get_matching_classes(csvreader_2007, csvreader_2015):
	matching_class = set()
	for row_07 in csvreader_2007[1:]:
		row_07 = list(row_07)
		row_07_class = (row_07[0]).replace(' ', '') + ' ' + row_07[1].strip(' ')
		
		for row_15 in csvreader_2015[1:]:
			row_15 = list(row_15)

			row_15_class = (row_15[2]).replace(' ', '') + ' ' + row_15[4]
			if row_07_class == row_15_class:
				matching_class.add(row_15_class)
	return matching_class

def get_grade_tuple(csvreader_2007, csvreader_2015, className):
	num_A_07 = 0
	num_A_minus_07 = 0
	num_A_plus_07 = 0
	num_B_07 = 0
	num_B_minus_07 = 0
	num_B_plus_07 = 0
	num_C_07 = 0
	num_C_minus_07 = 0
	num_C_plus_07 = 0
	num_D_07 = 0
	num_D_minus_07 = 0
	num_D_plus_07 = 0
	num_F_07 = 0

	num_A_15 = 0
	num_A_minus_15 = 0
	num_A_plus_15 = 0
	num_B_15 = 0
	num_B_minus_15 = 0
	num_B_plus_15 = 0
	num_C_15 = 0
	num_C_minus_15 = 0
	num_C_plus_15 = 0
	num_D_15 = 0
	num_D_minus_15 = 0
	num_D_plus_15 = 0
	num_F_15 = 0

	abbrev = className.split(' ')[0]
	class_num = className.split(' ')[1]

	for row in csvreader_2007[1:]:
		row = list(row)
		if abbrev == row[0].replace(' ', '') and class_num == str(row[1]):
			num_A_plus_07 += int(row[5])
			num_A_07 += int(row[6])
			num_A_minus_07 += int(row[7])
			num_B_plus_07 += int(row[8])
			num_B_07 += int(row[9])
			num_B_minus_07 += int(row[10])
			num_C_plus_07 += int(row[11])
			num_C_07 += int(row[12])
			num_C_minus_07 += int(row[13])
			num_D_plus_07 += int(row[14])
			num_D_07 += int(row[15])
			num_D_minus_07 += int(row[16])
			num_F_07 += int(row[17])
	for row in csvreader_2015[1:]:
		row = list(row)
		if abbrev == row[2].replace(' ', '') and class_num == str(row[4]):
			if row[9] != '':
				num_A_plus_15 += int(row[9])
			if row[10] != '':
				num_A_15 += int(row[10])
			if row[11] != '':
				num_A_minus_15 += int(row[11])
			if row[12] != '':
				num_B_plus_15 += int(row[12])
			if row[13] != '':
				num_B_15 += int(row[13])
			if row[14] != '':
				num_B_minus_15 += int(row[14])
			if row[15] != '':
				num_C_plus_15 += int(row[15])
			if row[16] != '':
				num_C_15 += int(row[16])
			if row[17] != '':
				num_C_minus_15 += int(row[17])	
			if row[18] != '':
				num_D_plus_15 += int(row[18])
			if row[19] != '':
				num_D_15 += int(row[19])
			if row[20] != '':
				num_D_minus_15 += int(row[20])		
			if row[21] != '':
				num_F_15 += int(row[21]) 

	grade_list_07 = (num_A_plus_07, num_A_07, num_A_minus_07, num_B_plus_07, num_B_07, num_B_minus_07, num_C_plus_07, num_C_07, num_C_minus_07, num_D_plus_07, num_D_07, num_D_minus_07, num_F_07)
	grade_list_15 = (num_A_plus_15, num_A_15, num_A_minus_15, num_B_plus_15, num_B_15, num_B_minus_15, num_C_plus_15, num_C_15, num_C_minus_15, num_D_plus_15, num_D_15, num_D_minus_15, num_F_15)

	return grade_list_07, grade_list_15

def largestClassIncrease(grade_dict):
	enrollment_increase = {}
	for className in grade_dict:
		enroll_07 = 0
		enroll_15 = 0
		for grade_bin_07 in grade_dict[className][0]:
			enroll_07 += grade_bin_07
		for grade_bin_15 in grade_dict[className][1]:
			enroll_15 += grade_bin_15
		percent_change = (enroll_15 - enroll_07) * 100./ enroll_07 
		enrollment_increase[className] = percent_change
	return OrderedDict(sorted(enrollment_increase.items(), key=lambda t:t[1]))

def aProportionIncrease(grade_dict):
	a_proportion_increase = {}
	for className in grade_dict:
		a_prop_07 = 0
		a_prop_15 = 0
		enroll_07 = 0
		enroll_15 = 0
		for grade_bin_07 in grade_dict[className][0]:
			enroll_07 += grade_bin_07
		for grade_bin_15 in grade_dict[className][1]:
			enroll_15 += grade_bin_15
		a_prop_07 = (grade_dict[className][0][0] + grade_dict[className][0][1] + grade_dict[className][0][2]) * 1./ enroll_07
		a_prop_15 = (grade_dict[className][1][0] + grade_dict[className][1][1] + grade_dict[className][1][2]) * 1./ enroll_15
		percent_change = (a_prop_15- a_prop_07) * 100./a_prop_07
		a_proportion_increase[className] = percent_change
	return OrderedDict(sorted(a_proportion_increase.items(), key=lambda t:t[1]))

def GPAIncrease(grade_dict):
	gpa_increase = {}
	for className in grade_dict:
		avg_gpa_07 = 0
		avg_gpa_15 = 0
		gpa_07 = calcGPA(grade_dict[className][0])
		gpa_15 = calcGPA(grade_dict[className][1])
		enroll_07 = 0
		enroll_15 = 0
		for grade_bin_07 in grade_dict[className][0]:
			enroll_07 += grade_bin_07
		for grade_bin_15 in grade_dict[className][1]:
			enroll_15 += grade_bin_15
		avg_gpa_07 = gpa_07/enroll_07
		avg_gpa_15 = gpa_15/enroll_15
		percent_change = (avg_gpa_15- avg_gpa_07) * 100. /avg_gpa_07
		gpa_increase[className] = percent_change
	return OrderedDict(sorted(gpa_increase.items(), key=lambda t:t[1]))

def calcGPA(grades):
	gpa = (grades[0] + grades[1]) * 4.0 + grades[2]* 3.7 + grades[3] * 3.3 + grades[4] *3.0 + grades[5] * 2.7 + grades[6] * 2.3 + grades[7] * 2.0 + grades[8] * 1.7 + grades[9] * 1.3 + grades[10] * 1.0 + grades[11]* 0.7
	return gpa

def getDepts(matching_classes):
	all_depts = set()
	for className in matching_classes:
		dept = className.split(' ')[0]
		all_depts.add(dept)
	return all_depts

def increaseDeptEnrollment(grade_dict, all_depts):
	enrollment_increase = {}
	for dept in all_depts:
		total_enrollment_07 = 0
		total_enrollment_15 = 0
		for className in grade_dict:
			if dept in className:
				for grade_bin_07 in grade_dict[className][0]:
					total_enrollment_07 += grade_bin_07
				for grade_bin_15 in grade_dict[className][1]:
					total_enrollment_15 += grade_bin_15
		percent_change = (total_enrollment_15 - total_enrollment_07) * 100./total_enrollment_07
		enrollment_increase[dept] = percent_change
	return OrderedDict(sorted(enrollment_increase.items(), key=lambda t:t[1]))

def getDeptGPAIncrease(grade_dict, all_depts):
	gpa_increase = {}
	for dept in all_depts:
		total_enrollment_07 = 0
		total_enrollment_15 = 0
		total_A_07 = 0
		total_A_minus_07 = 0
		total_A_plus_07 = 0
		total_B_07 = 0
		total_B_minus_07 = 0
		total_B_plus_07 = 0
		total_C_07 = 0
		total_C_minus_07 = 0
		total_C_plus_07 = 0
		total_D_07 = 0
		total_D_minus_07 = 0
		total_D_plus_07 = 0
		total_F_07 = 0

		total_A_15 = 0
		total_A_minus_15 = 0
		total_A_plus_15 = 0
		total_B_15 = 0
		total_B_minus_15 = 0
		total_B_plus_15 = 0
		total_C_15 = 0
		total_C_minus_15 = 0
		total_C_plus_15 = 0
		total_D_15 = 0
		total_D_minus_15 = 0
		total_D_plus_15 = 0
		total_F_15 = 0
		for className in grade_dict:
			if dept in className:
				for grade_bin_07 in grade_dict[className][0]:
					total_enrollment_07 += grade_bin_07
				for grade_bin_15 in grade_dict[className][1]:
					total_enrollment_15 += grade_bin_15
				total_A_07 += grade_dict[className][0][1]
				total_A_minus_07 += grade_dict[className][0][2]
				total_A_plus_07 += grade_dict[className][0][0]
				total_B_07 += grade_dict[className][0][4]
				total_B_minus_07 += grade_dict[className][0][5]
				total_B_plus_07 += grade_dict[className][0][3]
				total_C_07 += grade_dict[className][0][7]
				total_C_minus_07 += grade_dict[className][0][8]
				total_C_plus_07 += grade_dict[className][0][6]
				total_D_07 += grade_dict[className][0][10]
				total_D_minus_07 += grade_dict[className][0][11]
				total_D_plus_07 += grade_dict[className][0][9]
				total_F_07 += grade_dict[className][0][12]

				total_A_15 += grade_dict[className][1][1]
				total_A_minus_15 += grade_dict[className][1][2]
				total_A_plus_15 += grade_dict[className][1][0]
				total_B_15 += grade_dict[className][1][4]
				total_B_minus_15 += grade_dict[className][1][5]
				total_B_plus_15 += grade_dict[className][1][3]
				total_C_15 += grade_dict[className][1][7]
				total_C_minus_15 += grade_dict[className][1][8]
				total_C_plus_15 += grade_dict[className][1][6]
				total_D_15 += grade_dict[className][1][10]
				total_D_minus_15 += grade_dict[className][1][11]
				total_D_plus_15 += grade_dict[className][1][9]
				total_F_15 += grade_dict[className][1][12]
		total_grade_dist_07 = [total_A_plus_07, total_A_07, total_A_minus_07, total_B_plus_07, total_B_07, total_B_minus_07, total_C_plus_07, total_C_07, total_C_minus_07, total_D_plus_07, total_D_07, total_D_minus_07, total_F_07]
		total_grade_dist_15 = [total_A_plus_15, total_A_15, total_A_minus_15, total_B_plus_15, total_B_15, total_B_minus_15, total_C_plus_15, total_C_15, total_C_minus_15, total_D_plus_15, total_D_15, total_D_minus_15, total_F_15]
		total_gpa_07 = calcGPA(total_grade_dist_07)
		total_gpa_15 = calcGPA(total_grade_dist_15)

		avg_gpa_07 = total_gpa_07 / total_enrollment_07
		avg_gpa_15 = total_gpa_15 / total_enrollment_15

		percent_change = (avg_gpa_15 - avg_gpa_07) * 100./ avg_gpa_07
		gpa_increase[dept] = percent_change
	return OrderedDict(sorted(gpa_increase.items(), key=lambda t:t[1]))

def enrollmentChangeWithDept(grade_dict, dept):
	enrollment_increase = {}
	for className in grade_dict:
		if dept.upper() in className:
			enrollment_07 = 0
			enrollment_15 = 0
			for grade_bin_07 in grade_dict[className][0]:
				enrollment_07 += grade_bin_07
			for grade_bin_15 in grade_dict[className][1]:
				enrollment_15 += grade_bin_15
			percent_change = (enrollment_15 - enrollment_07) * 100./enrollment_07
			enrollment_increase[className] = percent_change
	return OrderedDict(sorted(enrollment_increase.items(), key=lambda t:t[1]))


fall_matching_classes = get_matching_classes(f_csvreader2007, f_csvreader2015)
spring_matching_classes = get_matching_classes(s_csvreader2007, s_csvreader2015)
fall_grade_dict = {}
spring_grade_dict = {}
for f_matching_class in fall_matching_classes:
	f_grade_2007, f_grade_2015 = get_grade_tuple(f_csvreader2007, f_csvreader2015, f_matching_class)
	fall_grade_dict[f_matching_class] = (f_grade_2007, f_grade_2015)

for s_matching_class in spring_matching_classes:
	s_grade_2007, s_grade_2015 = get_grade_tuple(s_csvreader2007, s_csvreader2015, s_matching_class)
	spring_grade_dict[s_matching_class] = (s_grade_2007, s_grade_2015)

f_all_depts = getDepts(fall_matching_classes)
s_all_depts = getDepts(spring_matching_classes)


# f_ordered_increasing_enrollment_dict = largestClassIncrease(fall_grade_dict)
# count = 10
# print 'Fall Top 10 in Enrollment Change'
# for key in f_ordered_increasing_enrollment_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in enrollment of ' + str(f_ordered_increasing_enrollment_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Fall Bottom 10 in Enrollment Change'
# count = len(f_ordered_increasing_enrollment_dict.keys())
# for key in f_ordered_increasing_enrollment_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in enrollment of ' + str(f_ordered_increasing_enrollment_dict[key]) + '%'
# 	count -= 1

# s_ordered_increasing_enrollment_dict = largestClassIncrease(spring_grade_dict)

# count = 10
# print "\n"
# print 'Spring Top 10 in Enrollment Change'
# for key in s_ordered_increasing_enrollment_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in enrollment of ' + str(s_ordered_increasing_enrollment_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Spring Bottom 10 in Enrollment Change'
# count = len(s_ordered_increasing_enrollment_dict.keys())
# for key in s_ordered_increasing_enrollment_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in enrollment of ' + str(s_ordered_increasing_enrollment_dict[key]) + '%'
# 	count -= 1

# f_ordered_a_prop_dict = aProportionIncrease(fall_grade_dict)

# count = 10
# print "\n"
# print 'Fall Top 10 in Proportion of As'
# for key in f_ordered_a_prop_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in amount of As ' + str(f_ordered_a_prop_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Fall Bottom 10 in Proportion of As'
# count = len(f_ordered_a_prop_dict.keys())
# for key in f_ordered_a_prop_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in amount of As by ' + str(f_ordered_a_prop_dict[key]) + '%'
# 	count -= 1

# s_ordered_a_prop_dict = aProportionIncrease(spring_grade_dict)

# count = 10
# print "\n"
# print 'Spring Top 10 in Proportion of As'
# for key in s_ordered_a_prop_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in amount of As ' + str(s_ordered_a_prop_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Spring Bottom 10 in Proportion of As'
# count = len(s_ordered_a_prop_dict.keys())
# for key in s_ordered_a_prop_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in amount of As by ' + str(s_ordered_a_prop_dict[key]) + '%'
# 	count -= 1

# f_ordered_gpa_dict = GPAIncrease(fall_grade_dict)

# count = 10
# print "\n"
# print 'Fall Top 10 in GPA Increase'
# for key in f_ordered_gpa_dict.keys()[-20:]:
# 	print str(count) + ': ' + key + ' with a change in amount of As ' + str(f_ordered_gpa_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Fall Bottom 10 in GPA Increase'
# count = len(f_ordered_gpa_dict.keys())
# for key in f_ordered_gpa_dict.keys()[:20]:
# 	print str(count) + ': ' + key + ' with a change in amount of As by ' + str(f_ordered_gpa_dict[key]) + '%'
# 	count -= 1

# s_ordered_gpa_dict = GPAIncrease(spring_grade_dict)

# count = 10
# print "\n"
# print 'Spring Top 10 in GPA Increase'
# for key in s_ordered_gpa_dict.keys()[-20:]:
# 	print str(count) + ': ' + key + ' with a change in amount of As ' + str(s_ordered_gpa_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Spring Bottom 10 in GPA Increase'
# count = len(s_ordered_gpa_dict.keys())
# for key in s_ordered_gpa_dict.keys()[:20]:
# 	print str(count) + ': ' + key + ' with a change in amount of As by ' + str(s_ordered_gpa_dict[key]) + '%'
# 	count -= 1

# f_ordered_dept_enrollment_dict = increaseDeptEnrollment(fall_grade_dict, f_all_depts)
# count = 10
# print "\n"
# print 'Fall Top 10 in Department Enrollment Change'
# for key in f_ordered_dept_enrollment_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in department enrollment of ' + str(f_ordered_dept_enrollment_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Fall Bottom 10 in Department Enrollment Change'
# count = len(f_ordered_dept_enrollment_dict.keys())
# for key in f_ordered_dept_enrollment_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in department enrollment of ' + str(f_ordered_dept_enrollment_dict[key]) + '%'
# 	count -= 1

# s_ordered_dept_enrollment_dict = increaseDeptEnrollment(spring_grade_dict, s_all_depts)

# count = 10
# print "\n"
# print 'Spring Top 10 in Department Enrollment Change'
# for key in s_ordered_dept_enrollment_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in department enrollment of ' + str(s_ordered_dept_enrollment_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Spring Bottom 10 in Department Enrollment Change'
# count = len(s_ordered_dept_enrollment_dict.keys())
# for key in s_ordered_dept_enrollment_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in department enrollment of ' + str(s_ordered_dept_enrollment_dict[key]) + '%'
# 	count -= 1

# f_dept_gpa_dict = getDeptGPAIncrease(fall_grade_dict, f_all_depts)

# count = 10
# print "\n"
# print 'Fall Top 10 departments in GPA Increase'
# for key in f_dept_gpa_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in amount of As ' + str(f_dept_gpa_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Fall Bottom 10 departments in GPA Increase'
# count = len(f_dept_gpa_dict.keys())
# for key in f_dept_gpa_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in amount of As by ' + str(f_dept_gpa_dict[key]) + '%'
# 	count -= 1

# s_dept_gpa_dict = getDeptGPAIncrease(spring_grade_dict, s_all_depts)

# count = 10
# print "\n"
# print 'Spring Top 10 departments in GPA Increase'
# for key in s_dept_gpa_dict.keys()[-10:]:
# 	print str(count) + ': ' + key + ' with a change in amount of As ' + str(s_dept_gpa_dict[key]) + '%'
# 	count -= 1
# print "\n"
# print 'Spring Bottom 10 departments in GPA Increase'
# count = len(s_dept_gpa_dict.keys())
# for key in s_dept_gpa_dict.keys()[:10]:
# 	print str(count) + ': ' + key + ' with a change in amount of As by ' + str(s_dept_gpa_dict[key]) + '%'
# 	count -= 1

# f_compsci_enrollment_dict = enrollmentChangeWithDept(fall_grade_dict, 'ECON')
# count = len(f_compsci_enrollment_dict)
# print '\n'
# print 'Fall Top 10 ECON Enrollment Increases'
# for key in f_compsci_enrollment_dict:
# 	print str(count) + ': ' + key + ' with enrollment change of ' + str(f_compsci_enrollment_dict[key]) +'%'
# 	count -= 1

# s_compsci_enrollment_dict = enrollmentChangeWithDept(spring_grade_dict, 'ECON')
# count = len(s_compsci_enrollment_dict)
# print '\n'
# print 'Spring Top 10 ECON Enrollment Increases'
# for key in s_compsci_enrollment_dict:
# 	print str(count) + ': ' + key + ' with enrollment change of ' + str(s_compsci_enrollment_dict[key]) +'%'
# 	count -= 1