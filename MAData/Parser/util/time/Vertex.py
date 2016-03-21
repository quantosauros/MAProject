'''
Created on 2015. 8. 18.

@author: Jay
'''

class Vertex():
    
    m_year = 0
    m_month = 0
    m_day = 0
    m_code = ""
    
    supportedVertices = {
             "D0" : "000000",
             "D1" :  "000001",
             "W1" :  "000007",
             "W2" :  "000014",
             "D15" :  "000015",
             "M1" :  "000100",
             "M2" :  "000200",
             "M3" :  "000300",
             "M4" :  "000400",
             "M5" :  "000500",
             "M6" :  "000600",
             "M7" :  "000700",
             "M8" :  "000800",
             "M9" :  "000900",
             "M10" :  "001000",
             "M11" :  "001100",
             "Y1" :  "010000",
             "Y1Q" :  "010300",
             "Y1H" :  "010600",
             "Y1T" :  "010900",
             "Y2" :  "020000",
             "Y2Q" :  "020300",
             "Y2H" :  "020600",
             "Y2T" :  "020900",
             "Y3" :  "030000",
             "Y3Q" :  "030300",
             "Y3H" :  "030600",
             "Y3T" :  "030900",
             "Y4" :  "040000",
             "Y4Q" :  "040300",
             "Y4H" :  "040600",
             "Y4T" :  "040900",
             "Y5" :  "050000",
             "Y5Q" :  "050300",
             "Y5H" :  "050600",
             "Y5T" :  "050900",
             "Y6" :  "060000",
             "Y6Q" :  "060300",
             "Y6H" :  "060600",
             "Y6T" :  "060900",
             "Y7" :  "070000",
             "Y7Q" :  "070300",
             "Y7H" :  "070600",
             "Y7T" :  "070900",
             "Y8" :  "080000",
             "Y8Q" :  "080300",
             "Y8H" :  "080600",
             "Y8T" :  "080900",
             "Y9" :  "090000",
             "Y9Q" :  "090300",
             "Y9H" :  "090600",
             "Y9T" :  "090900",
             "Y10" :  "100000",
             "Y12" :  "120000",
             "Y15" :  "150000",
             "Y20" :  "200000",
             "Y30" :  "300000",
        }
    supportedVertexMap = {}
     
    def __init__(self, code, value):
       
       self.m_code = code
       self.m_year = int(value[:2])
       self.m_month = int(value[2:4])
       self.m_day = int(value[4:6])
       #print self.m_year, self.m_month, self.m_day
    
    def __str__(self):
        return self.m_code
    
    @staticmethod
    def valueOf(code):
        if code in Vertex.supportedVertices :
            return Vertex(code, Vertex.supportedVertices[code])
        
        print "ERROR: Unsupported Vertex [" + code + "]"
        return None
    
    def getVertex(self):
        #print self.m_day, self.m_month, self.m_year
        return self.m_day / 365.0 + self.m_month / 12.0 + self.m_year 
    
    def getYear(self):
        return self.m_year
    
    def getMonth(self):
        return self.m_month
    
    def getDay(self):
        return self.m_day
    
    
    
    