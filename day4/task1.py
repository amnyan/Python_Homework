# create dictionary which has a six element(key,value)
students = {
  "student1_name" : 10,
  "student2_name" : 9,
  "student3_name" : 9,
  "student4_name" : 7,
  "student5_name" : 8,
  "student6_name" : 9
}
#add new student in dictionary with using "update" method
students.update({"student7_name":8})
# change value "student1_name" to Zero
students["student1_name"] = 0
#delete "students1_name" in dictionary
del students["student5_name"]
#print all dictionary
print(students)
#print with using loop
#for key, value in students.items():
#  print(f"{key} - {value}")
