from datetime import datetime
import os.path
def main():
    ClientFileName=raw_input("Enter file name:")
    try:
        file=open(ClientFileName,'r')
    except IOError:
        error=raw_input("File \""+ClientFileName+"\" not found, press any key to exit")
    max_size=int(raw_input("Enter maximum file size"))
    files=[]
    curclient=[]
    curFile=[]
    curClientNo=0
    header=file.readline()
    first=file.readline()
    first=first.split(',')
    curClientNo=first[2]
    curclient.append(first)
    count=0
    for line in file.readlines():
        line=line.split(',')
        count+=1
        if line[2]==curClientNo:
            curclient.append(line)
        else:
            curClientNo=line[2]
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
        file.write(header)
        for client in subFile:
            for entry in client:
                file.write(','.join(entry))
        fileno+=1
if __name__ == "__main__":
    main()
    
