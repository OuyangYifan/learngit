import os

#get and show the current work directory

print(os.getcwd())

My_Dir = os.path.join('D:\\','SandBox_Dev','Git','dev')
print(My_Dir)
os.chdir(My_Dir)
print(os.getcwd())
        
