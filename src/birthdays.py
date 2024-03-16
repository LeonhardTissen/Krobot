from .seasonNames import seasonNames

birthdays = {
	"Spring": {
		4: "Kent",
		7: "Lewis",
		10: "Vincent",
		14: "Haley",
		18: "Pam",
		20: "Shane",
		26: "Pierre",
		27: "Emily"
	},
	"Summer": {
		4: "Jas",
		8: "Gus",
		10: "Maru",
		13: "Alex",
		17: "Sam",
		19: "Demetrius",
		22: "Dwarf",
		24: "Willy",
		26: "Leo"
	},
	"Fall": {
		2: "Penny",
		5: "Elliott",
		11: "Jodi",
		13: "Abigail",
		15: "Sandy",
		18: "Marnie",
		21: "Robin",
		24: "George"
	},
	"Winter": {
		1: "Krobus",
		3: "Linus",
		7: "Caroline",
		10: "Sebastian",
		14: "Harvey",
		17: "Wizard",
		20: "Evelyn",
		23: "Leah",
		26: "Clint"
	}
}

def getBirthday(day, seasonId):
	birthday = ""

	season = seasonNames[seasonId]
	
	# Check if the day is a birthday
	if day in birthdays[season]:
		birthday = birthdays[season][day]

		# Link to the Stardew Valley Wiki to get information about what the character likes
		return f"\n([{birthday}](https://stardewcommunitywiki.com/{birthday})'s Birthday :birthday:)"

	# If no birthday, return empty string
	return ""
