#dateobjclient

import dateobj

d = dateobj.Date(2016, 2, 27)
print('Day: ', d.day)

d2 = dateobj.Date.from_string('2016-02-27')
print('Day: ', d2.day)

d3 = dateobj.Date.today()
print('Day: ', d3.day)

