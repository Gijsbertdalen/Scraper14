import scraperwiki

html = scraperwiki.scrape('http://inmo.ie/6022')

import lxml.html

root = lxml.html.fromstring(html) # turn our HTML into an lxml object

tds = root.cssselect('tr') # get all the <td tags

for tr in tds:
  print tr.text_content() # just the text inside the HTML tag

for tr in tds:
  record = { "tr" : tr.text_content() } # column name and value
  scraperwiki.sqlite.save(["tr"], record) # save the records one by one
