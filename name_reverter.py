import os

folder = "emails"

for f in [x for x in os.listdir(folder) if x.endswith(".msg")]:
	my_f = os.path.join(folder, f)
	__, f = f.split("#", 1)
	new_f = os.path.join(folder, f)

	os.rename(my_f, new_f)