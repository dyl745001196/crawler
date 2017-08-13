import csv 



file = open('out.csv', 'r')
html = open('house.html','w+')
lines = csv.reader(file)
for line in lines:
	if len(line)>0:
		template = "<div>"+line[1]+"&nbsp;"+"<a style=\"color:#66ccff\"href="+line[3]+">"+line[2]+"</a></div>"
		print(template)
		html.write(template+'\n')