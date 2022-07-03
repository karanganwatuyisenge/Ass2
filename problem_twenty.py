marks=[[56,89,70,92,67,100],[60,70,100,45,70,76],[60,95,90,85,93,45],[55,80,56,45,51,76],[78,100,65,77,91,87],[45,78,65,50,45,87],[32,50,45,67,40,80]]
students=["Pelin","Dominique","Valentin","Christine","John Paul","Patrick","Kellen"]
subjects=["Algorithms and Data structures","Java","Web App Development","Databases","Human Computer Interaction","Information Retrieval"]
#This function help to calculate average of every students or marks he/she have in percentage
def is_passed(student):
    total=0
    for mark in student.values():
        total +=mark
    average=(total*100)/(len(student)*100)
    return (average,average>=50)
    
#This function helps to get or assign marks,subject to every students
def get_students_reports(marks,students,subjects):
    all_students=dict()
    for i in range(0,len(students)):
        score=dict()
        for num in range(0,len(marks[i])):
            score[subjects[num]]=marks[i][num]

        all_students[students[i]]=score
    return all_students

reports=get_students_reports(marks,students,subjects) #call get_students_reports function
#print student name and heir marks and decision if it is passed or failed
print('Student Name,Marks,Passed')
for student_name,student in reports.items():
    score,passed=is_passed(student)
    print(student_name.upper(),score,passed)

#print(get_students_reports(marks,students,subjects))

