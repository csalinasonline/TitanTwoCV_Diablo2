import requests
import os
import time
# Open a file
file = open("AssestListD2MonstersToDownload.txt", "r")

#
flag_dir = False
flag_dir2 = False
flag_files = False
flag_skip = False
path = ''
path2 = ''
fname = ''

# create parent directory path
parent_dir = 'Assets'
try:
    #pass
    os.mkdir(parent_dir)
except:
    pass

#
line = file.readline()
while line:
    line = file.readline()
    
    if '===' in line:
        flag_dir = True  
    
    if '---' in line:
        flag_dir2 = True      
        
    if flag_dir and '===' not in line:
        line = line.strip('\n')
        path = os.path.join(parent_dir, line)
        try:
            #pass
            os.mkdir(path)
        except:
            pass
        print(line)
        flag_dir = False
        
    if flag_dir2 and '---' not in line:
        line = line.strip('\n')
        line = line.strip(' ')
        fname = line
        #line = line.strip('(Diablo II)')
        path2 = os.path.join(path, line)
        try:
            #pass
            os.mkdir(path2)
        except:
            pass
        print(line)
        flag_dir2 = False  
        flag_files = True
        
    if flag_files:
        if '---' in line:
            flag_files = False
            flag_skip = True
        else:  
            if flag_skip:
                flag_skip = False
            else:
                line = line.strip('\n')
                line = line.strip(' ')    
                line_strip = line.split(',')
                #print(line_strip)
                if len(line_strip) == 2:
                    filename = fname + '-' + line_strip[0]
                    print(filename)
                    path3 = os.path.join(path2, filename + '.gif')
                    url =  line_strip[1]
                    #print(path3)
                    myfile = requests.get(url)
                    open(path3, 'wb').write(myfile.content)
                    time.sleep(1)
                if len(line_strip) == 3:
                    line_strip[1] = line_strip[1].strip(' ')
                    filename = fname + '-' + line_strip[0] + '-' + line_strip[1]
                    print(filename)
                    path3 = os.path.join(path2, filename + '.gif')
                    url =  line_strip[2]
                    #print(path3)
                    myfile = requests.get(url)
                    open(path3, 'wb').write(myfile.content)
                    time.sleep(1)     
                    
#              
file.close() 
