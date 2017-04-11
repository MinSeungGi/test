__author__='mike_bowles'
import urllib2
import sys

#UCI 데이터 레포지토리에서 데이터 읽기
target_url=("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bnch/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)

#레이블을 리스트로, 속성을 리스트의 리스트로 데이터 정돈

xList =[]
labels=[]

for line in data:
    #쉼표로 분리
    row =line.strip().split(",")
    xList.append(row)
nrow=len(xList)
ncol=len(xList[1])

type=[0]*3
colCounts=[]

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a,float):
                type[0] +=1
                
    except ValueError:
            if len(row[col]) >0:
                type[1] +=1
            else:
                type[2] += 1
    colCounts.append(type)
    type =[0]*3
sys.stdout.write('col#' + '\t' + "number" +'\t' + "Strings" +'\t' + "other\m")
iCol =0
for types in colCounts:
    sys.stdout.write(str(iCol)+'\t\t' + str(types[0] + '\t\t'+ str(type[1]) + '\t\t' + str(type[2]) +"\t")
    iCol +=1                
