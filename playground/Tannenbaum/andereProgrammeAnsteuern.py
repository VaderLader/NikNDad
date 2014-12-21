'''import xmasPrint

xmasPrint.xmasp('Test')
print('\n')
xmasPrint.xmasp('Test2', bye = 'Tschüss')'''

myFile = open('./HalloTanne.txt', 'r')

#print(myFile, '\n-----')

#print (myFile.readlines())

for l in myFile.readlines():
    print (l, end='\n')



print ('\n\n\nFinish')  
'''print (myFile.readlines()[0])
print (myFile.readlines()[1])
print (myFile.readlines()[2])
'''
input('\n\n\n---Zum beenden bestätigen---')
