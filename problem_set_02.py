# START PROBLEM SET 2
print('Problem Set 2 \n')

wellbeing_resources = 'Counseling and Psychological Services (CAPS)|734-764-8312, '\
'SilverCloud|, '\
'Dean of Students Office|734-764-7420, '\
'Office of Student Conflict Resolution|734-936-6308, '\
'Services for Students with Disabilities (SSD)|734-763-3000, '\
'Maize and Blue Cupboard (MBC)|734-936-2794, '\
'Ginsberg Center for Community Service Learning|734-763-3548, '\
'Sexual Assault Prevention and Awareness Center (SAPAC)|734-764-7771, '\
'Multi-ethnic Student Affairs (MESA)|734-763-9044, '\
'Spectrum Center|734-763-4186'
# PROBLEM 01 (30 points)
print('\nPROBLEM 01')

wellbeing = wellbeing_resources.split(', ')
#print(wellbeing)

health = wellbeing[0:2]
print(health)

academic = wellbeing[2:5]
#print(academic)

community = wellbeing[-5:-3]
#print(community)

marginalized_comm = wellbeing[-3:]
#print(marginalized_comm)

# PROBLEM 02 (40 points)
print('\nPROBLEM 02')
addl_health_resources = ['UMSI Embedded CAPS Psychologist|Ashley Evearitt',
'Wolverine Wellness|734-763-1320']

health.extend(addl_health_resources)
#print(health)

uhs = 'University Health Service (UHS)|734-764-8320'

health.append(uhs)

trotter = 'Trotter Multicultural Center|734-763-3670'

marginalized_comm.insert(1, trotter)
#print(marginalized_comm)

addl_academic_resources = ['Sweetland Center for Writing', 'Office of the Ombuds']
addl_academic_resource_numbers = ['|734-764-0429', '|734-763-3545']

addl_academic_resources[0] = addl_academic_resources[0] + addl_academic_resource_numbers[0]
addl_academic_resources[1] = addl_academic_resources[1] + addl_academic_resource_numbers[1]
#print(addl_academic_resources)

academic.extend(addl_academic_resources)
#print(academic)


# PROBLEM 03 (20 points)
print('\nPROBLEM 03')

health.reverse()
print(health)

academic.sort()
print(academic)

marginalized_comm.sort(reverse=True)
print(marginalized_comm)

umsi_caps = health.index("UMSI Embedded CAPS Psychologist|Ashley Evearitt")
print(umsi_caps)

student_focused_health_resources = health[-1:umsi_caps - 1]
print(student_focused_health_resources)

# PROBLEM 04 (10 points)
print('\nPROBLEM 04')

uhs = health[0]

# END PROBLEM SET