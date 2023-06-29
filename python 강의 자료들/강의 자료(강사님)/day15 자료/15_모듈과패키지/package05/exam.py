import sys

print(sys.path)
"""
['c:\\work\\pythonwork\\15_모듈과패키지\\package05', 
'C:\\Python\\Python311\\python311.zip', 
'C:\\Python\\Python311\\DLLs', 
'C:\\Python\\Python311\\Lib', 
'C:\\Python\\Python311', 
'C:\\Python\\Python311\\Lib\\site-packages']
"""
sys.path.append('D:\\my\\')
print(sys.path)
"""
['c:\\work\\pythonwork\\15_모듈과패키지\\package05', 
'C:\\Python\\Python311\\python311.zip', 
'C:\\Python\\Python311\\DLLs', 
'C:\\Python\\Python311\\Lib', 
'C:\\Python\\Python311', 
'C:\\Python\\Python311\\Lib\\site-packages', 
'D:\\my\\']
"""