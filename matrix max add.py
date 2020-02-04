# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:50:41 2020

@author: Ravit Ben David
"""

import numpy as np 




def main():
    arr1 = np.array([[1,2],[2,5],[4,8],[3,2]])
    arr2 = np.array([[5,7,3],[9,6,4],[1,2,7]])
    print(addmax(arr1,arr2))




def addmax(arr1,arr2):
    #טענת כניסה: הפעולה מקבלת 2 מטריצות ומחשבת את פעולת החיבור המקסימאלית של שתיהן 
    #טענת יציאה: הפעולה מחזירה מטריצה ובה תוצאת פעולת החיבור מהקסימלית 
    if(np.size(arr1,0)==np.size(arr2,0)and np.size(arr1,1)==np.size(arr2,1)):
        return arr1+arr2
    li3 = arr1.tolist()
    li4 = arr2.tolist() 
    maxlines =max(np.size(arr1,0),np.size(arr2,0))
    maxrows = max(np.size(arr1,1),np.size(arr2,1))
    minlines= min(np.size(arr1,0),np.size(arr2,0))
    minrows= min(np.size(arr1,1),np.size(arr2,1)) 
    for i in range (maxlines):
        if (i==0):
            newarr= np.array([calcList(minrows,maxrows,li3[i],li4[i])])
        elif(i<minlines):
            newarr =np.append(newarr,[calcList(minrows,maxrows,li3[i],li4[i])],0)
        if(i>=minlines):
            if(np.size(arr1,0)==maxlines):
                newarr =np.append(newarr,[calcList2(minrows,maxrows,li3[i])],0)
            else:
                newarr =np.append(newarr,[calcList2(minrows,maxrows,li4[i])],0)
    return newarr
        
        


def calcList2(minrows,maxrows,li1):
    #טענת כניסה: הפעולה מקבלת את המספר המינימלי של הטורים ואת המספר המקסימלי של השורות ושורה של מטריצה כאשר יש רק שורה ממטריצה אחת  
    #טענת יציאה: הפעולה מחזירה שורה ובה התוצאה 
    li=[]
    for i in range(maxrows):
        if (i<minrows):
            item=li1[i]
        else:
            if(len(li1)==maxrows):
                item=li1[i]
            else:
                item = 0
        li.append(item)
    return li          
  
            



def calcList(minrows,maxrows,li1,li2):
    #טענת כניסה: הפעולה מקבלת את הכמות המקסימלית של הטורים ואת הכמות המינימלית של טורים ושורה אחת מכל מטריצה 
    #טענת יציאה: הפעולה מחזירה שורה ובה תוצאה של פעולת החיבור 
    li=[]
    for i in range(maxrows):
        if(i<minrows):
            item=li1[i]+li2[i]
        if(i>=minrows):
            if(len(li1)>len(li2)):
                item=li1[i]
            else:
                item=li2[i]
        li.append(item)
    return li



if __name__ == "__main__":
    main()    

