marks = {"a": 1, "b": 2, "c": 3}        # in dictionary key is identifier which means it should be unique
                                        # value can be duplicate but key should be unique
                                        # if we try to add same key again, the prior value will be updated with new value
# marks.update({"d": 4, "e": 5,"a": 10})
# print(marks)


# ---> Interview Questions
# both are used to access value using key
# but get() method returns None if key not found
print(marks.get("a"))   # print none if key not found
print(marks["a"])       # KeyError if key not found


# ---> methods
# print(marks.items())
# print(marks.keys())
# print(marks.values())

# --> looping through dictionary
# for key, value in marks.items():
#     print(f"Key: {key}, Value: {value}")