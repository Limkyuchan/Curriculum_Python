year = int(input('태어난 년도를 입력하시오?'))
    
age = 2016 - year +1
if year<100:
    age -= 1900
if age>=100:
    age -= 100
    
print("{0:02d}년에 태어난 당신은 {1}살입니다.".format(year, age))
