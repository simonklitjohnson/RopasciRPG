
def save(quitgame=0):
	clear()
	if quitgame == 0:
		print("What would you like to call your savegame? (Type \"Back\" to go back to the menu)")
	else:
		print("What would you like to call your savegame?")
	filename = input("> ")
	filename = filename.lower()
	if filename == "back" and quitgame == 0:
		mg()
	elif filename == "back" and quitgame == 1:
		save(1)

	if not os.path.exists("saves"):
		os.makedirs("saves")

	file = pathlib.Path('saves/' + filename + ".rps")
	if file.exists():
		print("A savegame with this name already exists. Would you like to overwrite?\n1) Yes\n2) No")
		selection = input("> ")
		if selection == "1":
			f = open("saves/" + filename + ".rps", "wb")
			pickle.dump(player, f, pickle.HIGHEST_PROTOCOL) #dump object using pickle
			f.close()
			print("Your game has been saved. Press enter to continue.")
			enter = input("> ")
			if(quitgame == 0):
				if enter == "":
					mg()
				else:
					mg()
			else:
				gameexit()
		else:
			save()
	else:
		f = open("saves/" + filename + ".rps", "wb")
		pickle.dump(player, f, pickle.HIGHEST_PROTOCOL)
		f.close()
		print("Your game has been saved. Press enter to continue.")
		enter = input("> ")
		if(quitgame == 0):
			initiate()
		else:
			gameexit()

def load():
	clear()
	global player
	savedgames = []
	if os.path.exists("saves"):
		for file in os.listdir("saves"):
			if file.endswith(".rps"):
				savedgames.append(file[:-4])

	if not savedgames:
		print("No savegames exist. Press enter to return to the main menu.")
		enter = input("> ")
		initiate()
	else:
		print('The following savegames exist:\n%s' % '\t'.join(map(str, savedgames)) + "\nWhich one would you like to load? (type \"Back\" to return to the main menu)")
		loadfile = input("> ")
		if loadfile == "back":
			initiate()
		else:
			file = pathlib.Path('saves/' + loadfile + ".rps")
			if file.exists():
				with open('saves/' + loadfile + '.rps', 'rb') as f:
					player = pickle.load(f)
					createnoplayer()
				mg()
			else:
				load()
