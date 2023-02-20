import time

now = time.localtime()

#The watch (ASCII ART from: https://www.asciiart.eu/electronics/clocks ): 
top = r"""       ,--.-----.--.
       |--|-----|--|
       |--|     |--|
       |  |-----|  |
     __|--|     |--|__
    /  |  |-----|  |  \
   /   \__|-----|__/   \
  /   ______---______   \/\
 /   /               \   \/
{   /                 \   } """

mid = r"""
|  {     _     _   _   }  |-,
|  |    | | . | | | |  |  | |
|  {    |_| . |_| |_|  }  |-' """

botton = r"""{   \                 /   }
 \   `------___------'   /\
  \     __|-----|__     /\/
   \   /  |-----|  \   /
    \  |--|     |--|  /
     --|  |-----|  |--
       |--|     |--|
       |--|-----|--|
       `--'-----`--' """

#middle structur front (a) list
mida = [r"""|  {""", r"""|  |""", r"""|  {"""]
#middle structure back (b) list
midb = [r"""}  |-,""", r"""|  | |""", r"""}  |-'"""]

#doppel punkt
dp = [r""" """, r""".""", r"""."""]
#Nummer Matrix: number[i] = the actual number xD 
number = [[r""" _ """, r"""| |""", r"""|_|"""], [r"""   """, r"""/| """, r""" | """], [r""" _ """, r""" _|""", r"""|_ """], [r""" _ """, r""" _|""", r""" _|"""], [r"""   """, r"""|_|""", r"""  |"""], [r""" _ """, r"""|_ """, r""" _|"""], [r""" _ """, r"""|_ """, r"""|_|"""], [r"""__ """, r""" / """, r"""/  """], [r""" _ """, r"""|_|""", r"""|_|"""] , [r""" _ """, r"""|_|""", r""" _|"""]]

#Nummer Matrix: number[i] = the actual number xD But without the structure
Onumber = [[r'''   ,a8888a,     ''', r''' ,8P"'  `"Y8,   ''', r''',8P        Y8,  ''', r'''88          88  ''', r'''88          88  ''', r'''`8b        d8'  ''', r''' `8ba,  ,ad8'   ''', r'''   "Y8888P"     ''',], 
[r'''     88  ''', r'''   ,d88  ''', r''' 888888  ''', r'''     88  ''', r'''     88  ''', r'''     88  ''', r'''     88  ''', r'''     88  ''', r'''     88  '''], 
[r''' ad888888b,  ''', r'''d8"     "88  ''', r'''        a8P''', r'''     ,d8P"   ''', r'''   a8P"      ''', r''' a8P'        ''', r'''d8"          ''', r'''88888888888  '''], 
[r''' ad888888b,  ''', r'''d8"     "88  ''', r'''        a8P  ''',r'''      aad8"   ''', r'''     ""Y8,   ''', r'''        "8b  ''', r'''Y8,     a88  ''', r''' "Y888888P'  '''], 
[r'''        ,d8    ''', r'''      ,d888    ''',r'''    ,d8" 88    ''', r'''  ,d8"   88    ''', r''',d8"     88    ''', r'''8888888888888  ''', r'''         88    ''', r'''         88    '''],
[r'''8888888888   ''', r'''88           ''', r'''88  ____     ''', r'''88a8PPPP8b,  ''', r'''PP"     `8b  ''', r'''         d8  ''', r'''Y8a     a8P  ''', r''' "Y88888P"   '''], 
[r'''  ad8888ba,  ''', r'''8P'    "Y8  ''', r'''d8           ''', r'''88,dd888bb,  ''', r'''88P'    `8b  ''', r'''88       d8  ''', r'''88a     a8P  ''', r''' "Y88888P"   '''], 
[r'''888888888888  ''', r'''        ,8P'  ''', r'''       d8"    ''', r'''     ,8P'     ''', r'''    d8"       ''', r'''  ,8P'        ''',r'''  d8"          ''', r'''8P'           '''], 
[r''' ad88888ba   ''', r'''d8"     "8b  ''', r'''Y8a     a8P  ''', r''' "Y8aaa8P"   ''', r''' ,d8"""8b,   ''',r'''d8"     "8b  ''', r'''Y8a     a8P  ''', r''' "Y88888P"   '''], 
[r''' ad88888ba   ''', r'''d8"     "88  ''', r'''8P       88  ''', r'''Y8,    ,d88  ''', r''' "PPPPPP"88  ''', r'''         8P  ''', r'''8b,    a8P   ''', r'''`"Y8888P'    '''], ]
#Zeit finden:
	#Stunde finden (Zehner)
def find10():	
	if now.tm_hour < 10: 
		hour10 = 0
	elif now.tm_hour < 20: 
		hour10 = 1
	else:
		hour10 = 2
	#finden der minuten (Zehner)
	if now.tm_min < 10:
		min10 = 0
	elif now.tm_min < 20:
		min10 = 1
	elif now.tm_min < 30:
		min10 = 2
	elif now.tm_min < 40:
		min10 = 3
	elif now.tm_min < 50:
		min10 = 4
	elif now.tm_min < 60:
		min10 = 5
	return hour10, min10
def find():
	hour10, min10 = find10()
	n = hour10 * 10
	m = min10 * 10
	
	hour01 = now.tm_hour - n 
	min01 = now.tm_min - m
	return hour01, min01

#Ausgabe
#print(top)
#print(mid1a, number[1][0], number[1][0], dp[0], number[2][0], number[9][0], mid1b)
#print(mid2a, number[1][1], number[1][1], dp[1], number[2][1], number[9][1], mid2b)
#print(mid3a, number[1][2], number[1][2], dp[2], number[2][2], number[9][2], mid3b)
#print(botton)

hour10, min10 = find10()
hour01, min01 = find()
#print(mid1a, end=' ') 

def Uhr():
	i = 0
	print(top)
	while i<3:
		print(mida[i], number[hour10][i], number[hour01][i], dp[i], number[min10][i], number[min01][i], midb[i])
		i = i+1
	print(botton)

def ZeitOhneUhr():		
	j = 0
	while j<8:
		print(Onumber[hour10][j], Onumber[hour01][j], Onumber[min10][j], Onumber[min01][j])
		j = j+1

Uhr()
ZeitOhneUhr()
