#-*- coding: utf-8 -*-

import urllib2
import xml.etree.ElementTree as ET
from Parser.models import IrData

dateStr = "20150320"

xmlParam  = "\
<message>\
  <proframeHeader>\
    <pfmAppName>BIS-KOFIABOND</pfmAppName>\
    <pfmSvcName>BISIntFutSrchSO</pfmSvcName>\
    <pfmFnName>searchData</pfmFnName>\
  </proframeHeader>\
  <systemHeader></systemHeader>\
    <BISIntFutSrchDTO>\
    <tradeYmd>" + dateStr + "</tradeYmd>\
    <uGb>0</uGb>\
</BISIntFutSrchDTO>\
</message>"



r = urllib2.Request('http://www.kofiabond.or.kr/proframeWeb/XMLSERVICES/',
                data = xmlParam,
                headers={'Content-Type': 'application/xml'})

u = urllib2.urlopen(r)
response = u.read()

print response
# 
# tree = ET.ElementTree(ET.fromstring(response))
# note = tree.getroot()
# 
# for pp in note.iter("BISIntFutSrchDTO") :
#     name = pp.find('beforeDayClPrc').text
#     
#     name_eng = pp.find('standardPrice').text
#     
#     
#     print name, name_eng
    
    