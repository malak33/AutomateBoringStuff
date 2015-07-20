# characterCount.py

message = 'It was a bright cold day in April, and the clouds were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
