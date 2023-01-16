# code for list comprehension
nums = ['1', '11', '121', '232', '343', '454']
new_sequence = [x for x in nums if "1" in x]
print(new_sequence)
def showing_comprehension():
    new_list = [x if "1" not in x else "2" for x in nums]
    print(new_list)


showing_comprehension()
