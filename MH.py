# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:40:17 2017

@author: tedoreve
"""

import random as ran

#===============================character======================================
class character(object):
    
    def __init__(self,name,score,number):            
        self.name   = name
        self.pop    = score*number
        self.star   = self.pop/1000
        self.sssr   = 1000/self.pop
        
    def get_attr(self,liver):
        self.belief = self.pop*liver
#        self.life   = self.belief*self.pop
#        self.magic  = self.belief/self.pop

        
#===============================decoration=====================================
class accessory(object):
    
    def __init__(self,name,star,intro):
        self.name   = name
        self.star   = star
        self.intro  = intro

#=================================pool=========================================
class pool(object):
    
    def __init__(self):
        self.total  = 2
    
    def char_pool(self):
        pool        = []
        pool.append(character('荡漾',9,7000))
        pool.append(character('嘟嘟噜',9.5,8000))
        return pool
        
    def acce_pool(self):
        pool        = []
        pool.append(character('琴里的缎带',9,7000))
        pool.append(character('金属乌帕',9.5,8000))
        return pool
        

#=================================player=======================================
class player(object):
    
    def __init__(self,name,pwd,liver,pool):
        self.name   = name
        self.pwd    = pwd
        self.liver  = liver
        self.pool   = pool
        
    def roll(self):
        n           = ran.randint(0,len(self.pool)-1)
        print(self.pool[n].name)
        return self.pool[n]
      
        
#===================================main=======================================
if __name__=='__main__':

    char_pool      = pool().char_pool()
    zmf            = player('zmf','19910805','10000',char_pool)
#==============================================================================
