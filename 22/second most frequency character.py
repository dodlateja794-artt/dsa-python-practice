s = "aaabbbbcc"
count={}
for ch in s:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
max_char = ""
max_count = 0
second_char = ""
second_count = 0
for ch, value in count.items():
    if value > max_count:
        second_count = max_count
        second_char = max_char

        max_count = value
        max_char = ch

    elif value > second_count:

        second_count = value
        second_char = ch

print(second_char)