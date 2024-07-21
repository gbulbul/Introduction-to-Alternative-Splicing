# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 01:16:06 2024

@author: gbulb
"""
class Alternative_Splicing:
    def factorial_(n):
        if n==0 or n==1:
           return 1
        if n>=1:
           return n*Alternative_Splicing.factorial_(n-1)
    
    
    def calculation_(n,m):
        sum=0
        for i in range(m,n+1):
            sum+=Alternative_Splicing.factorial_(n)/Alternative_Splicing.factorial_(i)/Alternative_Splicing.factorial_(n-i)
        return sum
    
if __name__=="__main__":  
   n,m=6,3
   print(Alternative_Splicing.calculation_(n,m))


        
    