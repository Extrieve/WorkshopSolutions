string = input()
st = []
for l in string:
	if len(st) > 0 and st[-1] == l:
		st.pop()
	else:
		st.append(l)

print(''.join(st))