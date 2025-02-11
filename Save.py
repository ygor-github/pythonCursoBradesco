file = open('Document.txt','w')

file.write('Curso Python \n')
file.write('Bradesco Foundation Certification \n')
file.write('Aula Práctica')
file.close()


#File reading
reading = open('Document.txt','r')
print(reading.read())
reading.close()