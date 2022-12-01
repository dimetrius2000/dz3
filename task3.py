s = str(input("Введите строку:"))

print(f"Строка {s} имеет длину {len(s)} символов")
subs_set = set()
uniq_dict = {}


for i in range(len(s)):
    for j in range(len(s)-1 if i == 0 else len(s), i, -1):
        subs_set.add(hash(s[i:j]))
        print(s[i:j])
        uniq_dict[s[i:j]] = hash(s[i:j])

print(len(list(uniq_dict.keys())), list(uniq_dict.keys()))
print("Количество различных подстрок в этой строке:", len(subs_set))

