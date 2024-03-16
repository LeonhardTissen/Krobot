from .seasonNames import seasonNames

def getBirthday(day, seasonId):
	birthday = ""

	season = seasonNames[seasonId]
	if season == "Spring":
		if day == 4:
			birthday = "Kent"
		elif day == 7:
			birthday = "Lewis"
		elif day == 10:
			birthday = "Vincent"
		elif day == 14:
			birthday = "Haley"
		elif day == 18:
			birthday = "Pam"
		elif day == 20:
			birthday = "Shane"
		elif day == 26:
			birthday = "Pierre"
		elif day == 27:
			birthday = "Emily"
		
	elif season == "Summer":
		if day == 4:
			birthday = "Jas"
		elif day == 8:
			birthday = "Gus"
		elif day == 10:
			birthday = "Maru"
		elif day == 13:
			birthday = "Alex"
		elif day == 17:
			birthday = "Sam"
		elif day == 19:
			birthday = "Demetrius"
		elif day == 22:
			birthday = "Dwarf"
		elif day == 24:
			birthday = "Willy"
		elif day == 26:
			birthday = "Leo"
	
	elif season == "Fall":
		if day == 2:
			birthday = "Penny"
		elif day == 5:
			birthday = "Elliott"
		elif day == 11:
			birthday = "Jodi"
		elif day == 13:
			birthday = "Abigail"
		elif day == 15:
			birthday = "Sandy"
		elif day == 18:
			birthday = "Marnie"
		elif day == 21:
			birthday = "Robin"
		elif day == 24:
			birthday = "George"
	
	elif season == "Winter":
		if day == 1:
			birthday = "Krobus"
		elif day == 3:
			birthday = "Linus"
		elif day == 7:
			birthday = "Caroline"
		elif day == 10:
			birthday = "Sebastian"
		elif day == 14:
			birthday = "Harvey"
		elif day == 17:
			birthday = "Wizard"
		elif day == 20:
			birthday = "Evelyn"
		elif day == 23:
			birthday = "Leah"
		elif day == 26:
			birthday = "Clint"
		

	if birthday != "":
		return f"\n([{birthday}](https://stardewcommunitywiki.com/{birthday})'s Birthday :birthday:)"

	return ""
