# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:23:21 2020

@author: Ravit Ben David
"""

import numpy as np




def main():
    
    arr1 = np.array([[1, 2, 3],[2, 5, 4]])
    arr2 = np.array([[5,7],[9,6],[1,2]])
    print(matmull(arr1,arr2))
    

def matmull(arr1,arr2):#פעולה שמחזירה את התוצאה הסופית של המכפלה  
    #טענת כניסה: פעולה מקבלת 2 מטריצות
#טענת יציאה: הפעולה מחזירה מטריעה בה נמצאת תוצאת המכפלה בין 2 המטריצות
    li=arr1.tolist()
    for i in range(np.size(arr1,0)):
        if (i==0):
            newarray= np.array([calcList(li[i],arr2)])
        else:
            newarray = np.append(newarray,[calcList(li[i],arr2)],0)
    return newarray



def calcitem(li1,li2):#מחשב את הערך של איבר אחד 
#טענת כניסה: הפעולה מקבלת שורה מן המטריצה הראשונה וטור מן המטריצה השנייה ומחשבת איבר במטריצה של התוצאה 
    #טענת יציאה: הפעולה מחזירה את האיבר בתוצאה שחושב 
    item=0
    for i in range (len(li1)):
        item = item +li1[i]*li2[i]
    return item
    


def calcList(li1,arr2):#מחזירה שורה של התוצאה
    #טענת כניסה: הפעולה מקבלת שורה במטריצה הראשונה ואת המטריצה השנייה הפעולה יוצרת שורה של איברים המופיעים במטריצת התוצאה
# הפעולה צחזירה את השורה שיצרה- שורה במטריצת התוצאות
    li=[]
    for i in range(np.size(arr2,1)):
        li.append(calcitem(li1,arr2[:,i]))
        
    return li
    





    
if __name__ == "__main__":
    main()    

    