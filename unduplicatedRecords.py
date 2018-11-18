
with open("wyniki_all.csv", 'r') as f:
	lines = f.readlines()

#non_dup = list(set(lines))

non_dup = [lines[0]]
for line in lines:
	if line != non_dup[-1]:
		non_dup.append(line)

last_man = None
txts = []
for line in non_dup:
	if not line.strip():
		continue
	man, txt = line.split(',', 1)
	if man == last_man:
		txts.append(txt.strip())
	elif last_man == None:
		last_man = man
		txts.append(txt.strip())
	else:
		print("{}, {}".format(
			last_man, ' '.join(txts)
		))
		last_man = man
		txts = [txt.strip()]

print("{}, {}".format(
	last_man, ' '.join(txts)
))