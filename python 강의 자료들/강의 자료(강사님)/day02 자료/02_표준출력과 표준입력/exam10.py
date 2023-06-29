str = "   Hello Python World!   "
print("str.count('o'):<%d>" % str.count('o'))
print("str.find('o'):<%d>" % str.find('o'))
print("':'.join(str):<%s>" % ':'.join(str))
print("str.upper():<%s>" % str.upper())
print("str.lower():<%s>" % str.lower())
print("str.lstrip():<%s>" % str.lstrip())
print("str.strip():<%s>" % str.strip())
print("str.replace('Hello', 'Hi'): <%s>" % str.replace('Hello', "Hi"))
print("str.split():<%s>" % str.split())
print("str.split('o'):<%s>" % str.split('o'))

print("':'.join(str.split()):<%s>" % ':'.join(str.split()))
print("':'.join(str.split('o')):<%s>" % ':'.join(str.split('o')))
