#!/usr/bin/python

import pycurl
import urllib
import cStringIO
import re

# curl -s -d "numero=RR238555257LU" http://www.trackandtrace.lu/homepage.htm |grep -A 4 ucune

buf = cStringIO.StringIO()
verbose = 0
tracking_no = 'RR'+'238555257'+'LU'
start_no = 100000000
end_no = 999999999

for tracking_no in xrange(start_no,end_no):
	print 'RR'+str(tracking_no)+'LU'

c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.trackandtrace.lu/homepage.htm")
pf = {'numero': tracking_no}
c.setopt(c.POSTFIELDS, urllib.urlencode(pf))
c.setopt(c.VERBOSE, verbose)
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()
page = buf.getvalue()
trackable = re.findall('Aucune',page)
if 'Aucune' in trackable:
	False
else:
	print tracking_no


buf.close()
c.close()
