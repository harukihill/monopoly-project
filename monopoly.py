#monopoly.py

	

def dice():
	import random

	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	
	roll = dice1 + dice2


	return roll

def card_choose():
	import random
	choice = random.randint(1, 16)

def main():
	import random
	#prompt number of rolls
	num = int(input("Enter number of rolls: "))
	
	#list of board places
	list = []
	for i in range(1, 41):
		list.append(0)
	
	rolls = 0
	place = 0
	jail_counter = 0
	dice_list = []
	num_three_roll = 0
	past_go = 0
	
	while(rolls < num):
		place += dice()
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		dice_list.append(dice1)
		dice_list.append(dice2)

		#Same rolls three times
		if (len(dice_list) > 5):
			if (dice_list[rolls - 5] == dice_list[rolls - 4]) and (dice_list[rolls - 3] == dice_list[rolls - 2]) and (dice_list[rolls - 1] == dice_list[rolls]):
				place = 10
				num_three_roll += 1
		
		#Move past 'Go'
		if (place >= 40):
			place = (place % 40)
			past_go += 1
		

		#landed on chance
		if (place == 7) or (place == 22) or (place == 36):
			choice = card_choose()
			if (choice == 1):
				#Go
				place = 0
				past_go += 1
			elif(choice == 2):
				#Illinois Avenue
				if (place == 36):
					past_go += 1
				place = 24
				
			elif(choice == 3):
				#St. Charles Place
				if (place == 22) or (place == 36):
					past_go += 1
				place = 11
			elif(choice == 4):
				#Utility
				if (place == 7) or (place == 36):
					if (place == 36):
						past_go += 1
					place = 12
				elif (place == 22):
					place = 28
			elif(choice == 5):
				#Railroad
				if (place == 7):
					place = 15
				elif(place == 22):
					place = 25
				else:
					place = 5
					past_go += 1
			elif(choice == 6):
				#Go back three spaces
				place = place - 3
			elif(choice == 7):
				#Jail
				place = 10
				jail_counter += 1
			elif(choice == 8):
				#Boardwalk
				place = 39
			
			
		

		#landed on community chest
		if (place == 2) or (place == 17) or (place == 33):
			choice = card_choose()
			if (choice == 1):
				#Go
				place = 0
				past_go += 1
			elif(choice == 2):
				#Jail
				place = 10
				jail_counter += 1
			
			

		#landed on 'Go To Jail'
		if (place == 30):
			place = 10
			jail_counter += 1
		
		# Record place
		list[place] += 1

		rolls += 1 
	print(list)

	# return place of most landed space
	top = 0
	place_high = 0
	for i in range(len(list)):
		if (list[i] > top) and (i != 10):
			top = list[i]
			place_high = i
	# return place of least landed space
	bottom = list[0]
	place_low = 0
	for i in range(len(list)):
		if (list[i] < bottom) and (i != 30):
			bottom = list[i]
			place_low = i
	
	print("\nThe space with the most hits is", str(place_high))
	print("The space with the least hits is", str(place_low))
	print("\nIn", str(num), "rolls, the roller has gone to jail", str(jail_counter),"times", 
"\nwhich is", str(round(jail_counter/num * 100,2)), "percent of rolls\n")

	#print number of past go
	print("Number of times passing 'Go': " + str(past_go))
	
	#print number of triple doubles
	print("Number of triple doubles: "+ str(num_three_roll) +"\n")
	
	#print percentages
	for i in range(len(list)):
		print_num = round(list[i] / num*100, 3)
		print(str(i) + ":", str(print_num))
	
	
main()
