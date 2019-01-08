from dijkstra import Graph
import os
import json
import sys 
g= Graph()
 
graph = [
[0, 150, 200, 0, 0, 0, 0],
[150, 0, 100, 60, 70, 0, 0],
[200, 100, 0, 0, 0, 80, 90],
[0, 60, 0, 0, 10, 0, 0],
[0, 70, 0, 10, 0, 20, 0],
[0, 0, 80, 0, 20, 0, 30],
[0, 0, 90, 0, 0, 30, 0]
]

start = raw_input("Enter the ip of start host: ")
end = raw_input("Enter the ip of end host: ")
z = input("Enter the bandwidth: ")

command = "curl -s http://192.168.56.1:8080/wm/device/?ipv4=%s" % (start)
result = os.popen(command).read()
parsedResult1 = json.loads(result)
x= parsedResult1['devices'][0]['attachmentPoint'][0]['switch']
x=x[-1]
x=int(x)-1
command = "curl -s http://192.168.56.1:8080/wm/device/?ipv4=%s" % (end)
result = os.popen(command).read()
parsedResult2 = json.loads(result)
y= parsedResult2['devices'][0]['attachmentPoint'][0]['switch']
y=y[-1]
y=int(y)-1
#x: number of src switch
#y: number of dst switch
path =[]
path=g.dijkstra(graph,x,y,z)
for i in range(len(path)):
    path[i]=path[i]+1


command = "curl -s http://192.168.56.1:8080/wm/topology/links/json"
result = os.popen(command).read()
parsedResult = json.loads(result)
j=0
srcPort=0
dstPort=0


if start == end or len(path) == 1:
    print "please check your input"
    sys.exit()

for i in range(len(path)):
    print path[i]

for i in range(len(path)):
    if  i==len(path)-1:
        for k in range(len(parsedResult)):        
            if parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i-1]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]):
                srcPort=parsedResult[k]['dst-port']

            elif parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i-1]):
                srcPort=parsedResult[k]['src-port']
        dstPort= parsedResult2['devices'][0]['attachmentPoint'][0]['port']
        dstPort=int(dstPort)
        cmd = "curl -X POST -d '{\"switch\":\"00:00:00:00:00:00:00:0%d\", \"name\":\"vc%d\", \"cookie\":\"0\", \"priority\":\"32768\",\"eth_type\":\"0x0800\" ,\"ipv4_src\":\"%s\",\"ipv4_dst\":\"%s\",\"active\":\"true\", \"actions\":\"output=%d\"}' http://192.168.56.1:8080/wm/staticflowpusher/json" %(path[i],j,start,end,dstPort)    
        result = os.popen(cmd).read()
        cmd = "curl -X POST -d '{\"switch\":\"00:00:00:00:00:00:00:0%d\", \"name\":\"vc%d\", \"cookie\":\"0\", \"priority\":\"32768\",\"eth_type\":\"0x0800\" , \"ipv4_dst\":\"%s\",\"ipv4_src\":\"%s\",\"active\":\"true\", \"actions\":\"output=%d\"}' http://192.168.56.1:8080/wm/staticflowpusher/json" %(path[i],j+1,start,end,srcPort)    
        result = os.popen(cmd).read()
        j+=2
        continue
    elif i==0:
        for k in range(len(parsedResult)):        
            if parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i+1]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]):
                dstPort=parsedResult[k]['dst-port']
            elif parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i+1]):
                dstPort=parsedResult[k]['src-port']
        srcPort= parsedResult1['devices'][0]['attachmentPoint'][0]['port']  
        srcPort=int(srcPort)
        cmd = "curl -X POST -d '{\"switch\":\"00:00:00:00:00:00:00:0%d\", \"name\":\"vc%d\", \"cookie\":\"0\", \"priority\":\"32768\",\"eth_type\":\"0x0800\" , \"ipv4_src\":\"%s\",\"ipv4_dst\":\"%s\",\"active\":\"true\", \"actions\":\"output=%d\"}' http://192.168.56.1:8080/wm/staticflowpusher/json" %(path[i],j,start,end,dstPort)    
        result = os.popen(cmd).read()
        cmd = "curl -X POST -d '{\"switch\":\"00:00:00:00:00:00:00:0%d\", \"name\":\"vc%d\", \"cookie\":\"0\", \"priority\":\"32768\",\"eth_type\":\"0x0800\" , \"ipv4_dst\":\"%s\",\"ipv4_src\":\"%s\",\"active\":\"true\", \"actions\":\"output=%d\"}' http://192.168.56.1:8080/wm/staticflowpusher/json" %(path[i],j+1,start,end,srcPort)    
        result = os.popen(cmd).read()
        j+=2
        continue
    for k in range(len(parsedResult)):
        if parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i-1]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]):
            srcPort=parsedResult[k]['dst-port']

        elif parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i-1]):
            srcPort=parsedResult[k]['src-port']
               
        elif parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i+1]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]):
            dstPort=parsedResult[k]['dst-port']
        elif parsedResult[k]['src-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i]) and parsedResult[k]['dst-switch'] == "00:00:00:00:00:00:00:0%d" %( path[i+1]):
            dstPort=parsedResult[k]['src-port']
    '''
    print "================================"
    print "switch is: ",path[i]    
    print "source port: ",srcPort
    print "destenation port: ",dstPort
    print "================================"
    '''
    cmd1 = "curl -X POST -d '{\"switch\":\"00:00:00:00:00:00:00:0%d\", \"name\":\"vc%d\", \"cookie\":\"0\", \"priority\":\"32768\",\"eth_type\":\"0x0800\" , \"ipv4_src\":\"%s\",\"ipv4_dst\":\"%s\",\"active\":\"true\", \"actions\":\"output=%d\"}' http://192.168.56.1:8080/wm/staticflowpusher/json" %(path[i],j,start,end,dstPort)    
    cmd2 = "curl -X POST -d '{\"switch\":\"00:00:00:00:00:00:00:0%d\", \"name\":\"vc%d\", \"cookie\":\"0\", \"priority\":\"32768\",\"eth_type\":\"0x0800\" , \"ipv4_dst\":\"%s\",\"ipv4_src\":\"%s\",\"active\":\"true\", \"actions\":\"output=%d\"}' http://192.168.56.1:8080/wm/staticflowpusher/json" %(path[i],j+1,start,end,srcPort)  
    result = os.popen(cmd1).read()
    result = os.popen(cmd2).read()
    j+=2      
