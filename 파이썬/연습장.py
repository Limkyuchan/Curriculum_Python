
from random import randint


for i in range(5):
    li = []
    while len(li) < 6:
        su = randint(1,45)
        if su not in li:
            li.append(su)

    print(li)


# for i in range(5):
#     li = []
#     lst = []
#     while len(li) < 6:
#         su = randint(1,45)
#         if su not in li:
#             li.append(su)
#     lst = sorted(li, key=lambda x:x)
    


#     print(lst)


#         {% for i in lst %}
#             <tr>
#                 <td>forloop.counter</td>
#             {% for j in i %}
#                 <td>{{ j }}</td>
#             {% endfor %}
#             </tr>
#         {% endfor %}