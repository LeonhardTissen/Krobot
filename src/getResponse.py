from .seasonNames import seasonNames
from .dates import dates
from .festivals import getFestival
from .birthdays import getBirthday
from .dateSpecifics import getDateSpecifics

def getResponse(seasonId, day, year):
	date = dates[day % 7]
	seasonName = seasonNames[seasonId]

	festival = getFestival(day, seasonId)
	birthday = getBirthday(day, seasonId)
	dateSpecifics = getDateSpecifics(date)

	return f"""Day {day} of {seasonName}, Year {year}, {date}{festival}{birthday}{dateSpecifics}"""
