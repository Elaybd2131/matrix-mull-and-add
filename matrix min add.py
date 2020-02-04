# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:18:13 2020

@author: Ravit Ben David
"""

import numpy as np 



def main():
    arr1 = np.array([[1, 2, 3],[2, 5, 4]])
    arr2 = np.array([[5,7],[9,6],[1,2]])
    print(addmin(arr1,arr2))



def addmin(arr1,arr2):
    #טענת כניסה: הפעולה מקבלת 2 מטריצות 
    #טענת יציאה: הפעולה מחזירה את המטריצה שבה תוצאת פעולת החיבור המינימלי
    if(np.size(arr1,0)==np.size(arr2,0)and np.size(arr1,1)==np.size(arr2,1)):
        return arr1+arr2
    li3 = arr1.tolist()
    li4 = arr2.tolist()    
    minlines= min(np.size(arr1,0),np.size(arr2,0))
    minrows= min(np.size(arr1,1),np.size(arr2,1))
    for i in range (minlines):
        if (i==0):
            newarr= np.array([calcList2(minrows,li3[i],li4[i])])
        else:
            newarr =np.append(newarr,[calcList2(minrows,li3[i],li4[i])],0)
    return newarr
        

        
        
        
def calcList2(num,li1,li2):
    #טענת כניסה: הפעולה מקבלת שורה מהמטריצה הראשונה והשנייה ומחזירה את השורה של התוצאה
    #טענת יציאה: הפעולה מחזירה שורה של התוצאה
    li=[]
    for i in range(num):
        item=li1[i]+li2[i]
        li.append(item)
    return li
        
        



if __name__ == "__main__":
    main()    
