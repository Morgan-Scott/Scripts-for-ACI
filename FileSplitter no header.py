from datetime import datetime
import os.path
def main():
    ClientFileName=raw_input("Enter file name (FILE MUST BE SORTED BY CUSTOMER NUMBER): ")
    try:
        file=open(ClientFileName,'r')
    except IOError:
        error=raw_input("File \""+ClientFileName+"\" not found, press any key to exit")
    max_size=int(raw_input("Enter maximum file size: "))
    files=[]
    curclient=[]
    curFile=[]
    curClientNo=0
    newCli=False
    test=raw_input("0")
    first=file.readline()
    first=first.split(',')
    test=raw_input("1")
    curClientNo=int(first[2])
    curclient.append(first)
    count=0
    test=raw_input("2")
    for line in file.readlines():
        line=line.split(',')
        count+=1
        if int(line[2])==curClientNo:
            curclient.append(line)
        else:
            newCli=raw_input("3")
            curClientNo=int(line[2])
            curFileSize=0
            for client in curFile:
                curFileSize+=len(client)

            if curFileSize+len(curclient)<max_size:
                
                curFile.append(curclient)
            else:
                files.append(curFile)
                curFile=[]
                curFile.append(curclient)
            curclient=[]
            curclient.append(line)
    curClientNo=line[2]
    curFileSize=0
    test=raw_input("4")
    for client in curFile:
        curFileSize+=len(client)
   
    if curFileSize+len(curclient)<max_size:        
        curFile.append(curclient)
        files.append(curFile)
    else:
        
        files.append(curFile)
        curFile=[]
        curFile.append(curclient)
        files.append(curFile)
    test=raw_input("5")
            
    file.close()
    fileno=1
    for subFile in files:
        if os.path.isfile(ClientFileName[:-4]+" "+str(fileno)+" of "+str(len(files))+".csv"):
           override=raw_input("This will overwrite an existing file, press '1' then 'Enter' to continue, or Press 'Enter' to Exit")
           if override !='1':
               return
        file=open(ClientFileName[:-4]+" "+str(fileno)+" of "+str(len(files))+".csv",'w')
        file.write('')
        file.close()
        file=open(ClientFileName[:-4]+" "+str(fileno)+" of "+str(len(files))+".csv",'a')
        checked=False
        if checked==False:
            checked=raw_input("6")
        for client in subFile:
            for entry in client:
                file.write(','.join(entry))
        fileno+=1
if __name__ == "__main__":
    main()
    
