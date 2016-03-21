'''
Created on 2015. 8. 15.

@author: jayjl
'''

class BusinessDayConvention():

    FOLLOWING = 0
    MODIFIED_FOLLOWING = 1
    PRECEDING = 2
    MODIFIED_PRECEDING = 3
    NEAREST = 4
    
    _code = 0
    _name = ""
    
    def __init__(self, code, name):
        '''
        Constructor
        '''
        self._code = code
        self._name = name
    
    @staticmethod
    def getInstance(code):
        if code is 0 :
            return BusinessDayConvention.FOLLOWING
        elif code is 1 :
            return BusinessDayConvention.MODIFIED_FOLLOWING
        elif code is 2 :
            return BusinessDayConvention.PRECEDING
        elif code is 3 :
            return BusinessDayConvention.MODIFIED_PRECEDING
        elif code is 4 :
            return BusinessDayConvention.NEAREST
        else :
            return None
        