import string
lower = string.ascii_lowercase
groups = {}

def generate_key(s):
    for char in lower:
        index = s.find(char)
        if index != -1:
            break
    key = s[index:] + s[:index]
    return key

def get_key(s, groups):
    ts = s
    rs = s[::-1]
    for i in xrange(len(s)):
        if ts in groups:
            return ts
        if rs in groups:
            return rs
        ts = ts[1:] + ts[:1]
        rs = rs[1:] + rs[:1]
    return None

prompt = 'Enter necklace: '
enter = raw_input(prompt)
while enter:
    key = get_key(enter, groups)
    if key is not None:
        groups[key].append(enter)
    else:
        key = generate_key(enter)
        groups[key] = [enter]

    enter = raw_input(prompt)

output_groups = sorted(groups.values(), key=len, reverse=True)
for g in output_groups:
    print ' '.join(sorted(g))