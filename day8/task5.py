strings_list = ["Hello", "Bye", "Hello", "Bye", "Bye", "okay"]

counts = {}

for string in strings_list:
    if string in counts:
        counts[string] += 1
    else:
        counts[string] = 1

for string, count in counts.items():
    print(f"'{string}' occurs {count} times.")