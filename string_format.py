#string_format.py

print('suf {:>10s}'.format('stuff'))
width=15
print('suf {:>{}s}'.format('stuff', width))
print('on the  {:>10s}'.format('same'), end=' ') # end works in python3
print(' {:>10s}'.format('line'))