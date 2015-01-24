#!/usr/bin/python

import pycurl
import urllib
import cStringIO
import sys
import re

# curl -s -d "numero=RR238555257LU" http://www.trackandtrace.lu/homepage.htm |grep -A 4 ucune

#tracking_no = 'RR'+'238555257'+'LU'
#start_no = 100000000

verbose = 0

start_no = 238555200
end_no = 999999999

for sequence in xrange(start_no,end_no):
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	c.setopt(pycurl.URL, "http://www.trackandtrace.lu/homepage.htm")
	c.setopt(c.VERBOSE, verbose)
	tracking_no = 'RR'+str(sequence)+'LU'
	pf = {'numero': tracking_no}
	c.setopt(c.POSTFIELDS, urllib.urlencode(pf))
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	page = buf.getvalue()
	trackable = re.findall('Aucune',page)
	if 'Aucune' in trackable:
		sys.stderr.write('BAD-'+tracking_no+'\n')
	else:
		print tracking_no
	buf.close()
	c.close()
