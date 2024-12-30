from fuzzywuzzy import fuzz,process

s1 = "She sells sea shells by the seashore"
s2 = "She sells sea shells on the seashore"

print("Fuzzy Ratio:",fuzz.ratio(s1,s2))
print("Fuzzy Partial Ratio",fuzz.partial_ratio(s1, s2))
print("Fuzzy Token Sort Ratio",fuzz.token_sort_ratio(s1, s2))
print("Fuzzy Token set Ratio",fuzz.token_set_ratio(s1, s2))

#process

query = "seashells by the seashore"
choices=["seashells on the seashore","she sells seashells","by the seashore"]

print("List of Ratio: ")
print(process.extract(query,choices))
print("Best among the list",process.extractOne(query,choices))