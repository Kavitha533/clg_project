import sys
import numpy as np 
import pandas as pd
a1=pd.read_csv("secondpatient.csv")
b1=a1[1::2]
b1
ca1=b1.iloc[:,:-1]
ca2=b1.iloc[:,-1]
la1=ca1.head(1)
from sklearn.linear_model import LogisticRegression 
classifier = LogisticRegression(random_state = 0) 
classifier.fit(ca1,ca2) 
def func(Age,Gender,Doctor_Id,Diagnosis):
    k=classifier.predict(np.array([[Age,Gender,Doctor_Id,Diagnosis]]))
    print(k)
    k=int(k)
    if(k==0):
        print('cured')
    elif(k==1):
        print('progress')
    else:
        print('notcured')
li=sys.argv
print(func(int(li[1]),int(li[2]),int(li[3]),int(li[4])))