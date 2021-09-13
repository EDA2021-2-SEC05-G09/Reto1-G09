from datetime import datetime

f1=datetime.strptime("1999-12-10","%Y/%m/%d" )
f2=datetime.strptime("1958/12/10","%Y/%m/%d" )
b=f1<f2
print(b)