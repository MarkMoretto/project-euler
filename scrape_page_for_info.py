
"""
Purpose: Scrape project-euler to get page info for recordkeeping
Date created: 2019-10-26

Contributor(s):
    Mark M.
"""

import re
import urllib.request as urequest

uri = r'https://projecteuler.net/problem=26'

with urequest.urlopen(uri) as req:
    data = str(req.read(), 'utf-8')

### Clean up \n, \r, spaces
data = re.sub(r'\s\s+', ' ', re.sub(r'(\n+|\r+)', ' ', data))

# Get main content
content_pat = r'\s<div\s+class\="problem_content"\srole\=".*?">(.*)<\/div><br>\s'
content = re.search(content_pat, data, re.I).group(1)



p_pat = r'<p>(.*)<\/p>'
p = re.compile(p_pat, re.M | re.I)
p_items = p.findall(data)



