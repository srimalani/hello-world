from random import randint
print("\nHello this is Raa and welcome to my version of \n**Rock** \n**Paper** \n**Scissors**")

num_players = int(input("How many would be paying today (1 or 2)? "))
while num_players != 1 and num_players != 2:
	num_players = int(input("Invalid response. \n  Type 1 or 2 - How many would be playing today? "))

num_games = int(input("How many games do you want to play? (between 1-10) "))
while num_games < 1 or num_games > 10:
	num_games = int(input("Invalid response. Type between 1 or 10 - How many games do you want to play? "))

p1_wins = 0
p2_wins = 0
p1name = ""
p2name = ""

while p1_wins < num_games//2+1 and p2_wins < num_games//2+1:
	
	if num_players == 1:
		if p1name == "" and p2name == "":
			p1name = input("What's your name Player 1 ?")
			p2name = "Computer"
		p1 = input(f"Whats you choice {p1name}? ").lower()
		while p1 != "rock" and p1 != "paper" and p1 != "scissors":
			print(f"Invalid input {p1name}. Type rock, paper or scissors? ")
			p1=str(input()).lower()
		p2 = randint(0,2)
		if p2==0:
			p2="rock"
		elif p2==1:
			p2="paper"
		elif p2==2:
			p2="scissors"
		print(f"Computer chooses {p2}")
		
		if(p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") or (p1=="scissors" and p2=="paper"):
			print(f"{p1name} wins")
			p1_wins += 1
		elif(p2=="rock" and p1=="scissors") or (p2=="paper" and p1=="rock") or (p2=="scissors" and p1=="paper"):
			print(f"{p2name} wins")
			p2_wins += 1
		else:
			print("Its a tie. Lets play again")	
		print(f" *** SCORE ***\n {p1name} {p2name} \n     {p1_wins}        {p2_wins} \n ****************")
	
	elif num_players == 2:
		if p1name == "" and p2name == "":
			p1name = input("What's your name Player 1 ?")
			p2name = input("What's your name Player 2 ?")
		p1 = input(f"Whats you choice {p1name}? ")
		while p1 != "rock" and p1 != "paper" and p1 != "scissors":
			print(f"Invalid input. Whats you choice {p1name}? ")
			p1=str(input()).lower()
		p2 = input(f"Whats you choice {p2name}? ")
		while p2 != "rock" and p2 != "paper" and p2 != "scissors":
			print(f"Invalid input. Whats you choice {p2name}? ")
			p2=str(input()).lower()

		if(p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="rock") or (p1=="scissors" and p2=="paper"):
			print(f"{p1name} wins")
			p1_wins += 1
		elif(p2=="rock" and p1=="scissors") or (p2=="paper" and p1=="rock") or (p2=="scissors" and p1=="paper"):
			print(f"{p2name} wins")
			p2_wins += 1
		else:
			print("Its a tie. Lets play again")
		print(f" *** SCORE ***\n {p1name} {p2name} \n     {p1_wins}        {p2_wins} \n ****************")
print("***********Final Score*************")
if p1_wins > p2_wins:
	print(f"{p1name} WINS")
else:
	print(f"{p2name} WINS")