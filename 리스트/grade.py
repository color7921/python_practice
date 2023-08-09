grade = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

for n,s in grade.items():
    print(f"{n}:{sum(s)/len(s)}")


text = "Hello, world!"

freq = {}

for c in text:
    if c not in freq.keys():
        freq[c] = 1
    else:
        freq[c] += 1
    
print(freq)
