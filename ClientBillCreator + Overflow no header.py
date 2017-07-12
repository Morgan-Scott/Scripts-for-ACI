from datetime import datetime
import os.path
def main():
    ClientFileName=raw_input("Enter client file name:")
    DataFileName=raw_input("Enter data file name:")
    try:
        file=open(ClientFileName,'r')
    except IOError:
        error=raw_input("Client file \""+ClientFileName+"\" not found, press any key to exit")
        return
    clients=[]
    otherLines=[]
    for line in file:
        clients.append([line.strip()])
    if len(clients)==0:
        error=raw_input("Client file \""+ClientFileName+"\" is empty, press any key to exit")
        return
    file.close()
    try:
        file=open(DataFileName,'r')
    except IOError:
        error=raw_input("Data file \""+DataFileName+"\" not found, press any key to exit")
        return
    for line in file:
        line=line.split(',')
        inList=False
        for client in clients:
            if client[0]==line[0]:
                client.append(line)
                inList=True
        if not inList:
            otherLines.append(line)
    file.close()
    for client in clients:
        if os.path.isfile(client[0]+" "+str(datetime.now().year)+"-"+str(datetime.now().month).zfill(2)+".csv"):
            override=raw_input("This will overwrite an existing file, press '1' then 'Enter' to continue, or Press 'Enter' to Exit")
            if override !='1':
                return
        file=open(client[0]+" "+str(datetime.now().year)+"-"+str(datetime.now().month).zfill(2)+".csv",'w')
        file.write('')
        file.close()
        file=open(client[0]+" "+str(datetime.now().year)+"-"+str(datetime.now().month).zfill(2)+".csv",'a')
        file.write(header)
        for entry in client[1:]:
           file.write(','.join(entry))
           #print ','.join(entry)
        file.close()
    if os.path.isfile("Working Copy "+str(datetime.now().year)+"-"+str(datetime.now().month).zfill(2)+".csv"):
            override=raw_input("This will overwrite an existing file, press '1' then 'Enter' to continue, or Press 'Enter' to Exit")
            if override=='1':
                return
    file=open("Working Copy "+str(datetime.now().year)+"-"+str(datetime.now().month).zfill(2)+".csv",'w')
    file.write('')
    file.close()
    file=open("Working Copy "+str(datetime.now().year)+"-"+str(datetime.now().month).zfill(2)+".csv",'a')
    for line in otherLines:
        file.write(','.join(line))
    
if __name__ == "__main__":
    main()
