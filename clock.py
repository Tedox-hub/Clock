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
print(top)
#print(mid1a, number[1][0], number[1][0], dp[0], number[2][0], number[9][0], mid1b)
#print(mid2a, number[1][1], number[1][1], dp[1], number[2][1], number[9][1], mid2b)
#print(mid3a, number[1][2], number[1][2], dp[2], number[2][2], number[9][2], mid3b)
#print(botton)

hour10, min10 = find10()
hour01, min01 = find()
#print(mid1a, end=' ') 
i = 0
while i<3: 
	print(mida[i], number[hour10][i], number[hour01][i], dp[i], number[min10][i], number[min01][i], midb[i])
	i = i+1
print(botton)
