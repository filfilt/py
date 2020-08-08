#To create a folder
import os
#os.mkdir('week3')
# os.mkdir('week4')
#os.makedirs('Student/Grade/11thGrade')

#To delete a folder
#os.rmdir('week4')
#os.rmdir('Student/Grade/9thGrade')

#r=>read, w=>write,x=>delete,a=>appand

f=open('student.txt','r')
print(f.read())

# f=open('student.txt','a')
# f.write('Ayele')