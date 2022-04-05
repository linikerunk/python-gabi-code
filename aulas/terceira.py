""" Listas de palavras reservadas 

 False	await	else	import	pass
 None	break	except	in	raise
 True	class	finally	is	return
 and	continue	for	lambda	try
 as	def	from	nonlocal	while
 assert	del	global	not	with
 async	elif	if	or	yield

>>> None == 0
False
>>> None == []
False
>>> None == False
False
>>> x = None
>>> y = None
>>> x == y
True

>>> a = 4
>>> assert a < 5
>>> assert a > 5

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

if True:
    print('Hello')
    a = 5

if True: print('Hello'); a = 5

def double(num):
    Function to double the value
    return 2*num
print(double.__doc__)

"""
# import keyword
# >>> print(keyword.kwlist)
