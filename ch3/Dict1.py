dict1 = {}
print(dict1)

lang = {'1':'Good Morning','2':'Hello'}
print(lang)

print('Number 1 is',lang['1'])

print('Number 1 is ',lang.get('1'))


#-----------#
lang['1'] = 'Hi'
print(lang)
lang['3'] = 'Student'
print(lang)

del lang['1']
print(lang)

lang.clear
print(lang)
