# dict = {
#     344 : "Vivek",
#     566 : "Shubham",
# }

# print(dict[344])

# print(dict)


# Dictionary is ordered

ep1 = {
    122:45,
    123 : 89,
    567 : 69,
    670 : 69
}

ep2 = {
        222 : 67 ,
          566 : 90
}


ep1.update(ep2)

ep1.pop(122)

#popitem removes last item

ep1.popitem()

print(ep1)


ep1.clear()
print(ep1)

empt = {}
print(empt)


