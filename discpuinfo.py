f = open('/proc/cpuinfo','r')
#print(f.read())
namedict = {'model name':'处理器：','cpu MHz':'主频：','cpu cores':'核心数量：'}
for each_line in f:
	(name, info) = each_line.split(':',1)
	print(namedict[name]+info)	
