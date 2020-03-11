def predict_match(team1,team2,match_map):
	import csv
	team_list=[team1,team2]
	separator=' '
	team1_diff=0
	team2_diff=0
	team1_score=0
	team2_score=0
	team2_won=f'Bet on {team2}!'
	team1_won=f'Bet on {team1}!'
	with open(f'{team1}.csv','r') as team1_file:
		reader=csv.reader(team1_file)
		count_win=0
		count_lose=0
		win_against=0
		lose_against=0
		for row in team1_file:
			row_list=row.split(',')
			if row_list[2]==match_map:
				score=row_list[3].split(' - ')
				score_diff=int(score[0])-int(score[1])
				team1_diff=team1_diff+score_diff
				if row_list[4]=='W':
					count_win+=1
				elif row_list[4]=='L':
					count_lose+=1
				if row_list[1]==team2:
					if row_list[4]=='W':
						win_against+=1
					elif row_list[4]=='L':
						lose_against+=1
		if win_against!=0 or lose_against!=0:
			team1_perc_against=(win_against*100)/(win_against+lose_against)
		else:
			team1_perc_against=0
		if count_win!=0 or count_lose!=0:
			team1_perc=(count_win*100)/(count_lose+count_win)
		else:
			team1_perc=0
	with open(f'{team2}.csv','r') as team1_file:
		reader=csv.reader(team1_file)
		count_win=0
		count_lose=0
		win_against=0
		lose_against=0
		for row in team1_file:
			row_list=row.split(',')
			if row_list[2]==match_map:
				score=row_list[3].split(' - ')
				score_diff=int(score[0])-int(score[1])
				team2_diff=team1_diff+score_diff
				if row_list[4]=='W':
					count_win+=1
				elif row_list[4]=='L':
					count_lose+=1
				if row_list[1]==team1:
					if row_list[4]=='W':
						win_against+=1
					elif row_list[4]=='L':
						lose_against+=1
		if win_against!=0 or lose_against!=0:
			team2_perc_against=(win_against*100)/(win_against+lose_against)
		else:
			team2_perc_against=0
		if count_win!=0 or count_lose!=0:
			team2_perc=(count_win*100)/(count_lose+count_win)
		else:
			team2_perc=0
	if team1_perc<45 and team1_perc<team2_perc:
		print(team2_won)
	elif team2_perc<45 and team2_perc<team1_perc:
		print(team1_won)
	elif team1_perc<team2_perc:
		team2_score+=1
	elif team2_perc<team1_perc:
		team1_score+=1
	elif team1_perc==team2_perc:
		team1_score+=1
		team2_score+=1
	if team1_diff<team2_diff:
		team2_score+=2
	elif team2_diff<team1_diff:
		team1_score+=2
	elif team1_diff==team2_diff:
		team1_score+=2
		team2_score+=2
	if team1_perc_against<team2_perc_against:
		team2_score+=2
	elif team2_perc_against<team1_perc_against:
		team1_score+=2
	elif team1_perc_against==team2_perc_against:
		team1_score+=2
		team2_score+=2
	if team1_score<team2_score:
		print(team2_won)
	elif team2_score<team1_score:
		print(team1_won)
	elif team1_score==team2_score:
		print("Don't bet on this match!!")
predict_match('Liquid','Natus Vincere','Mirage')
'''with open('Astralis.csv','r') as team1_file:
	reader=csv.reader(team1_file)
	for row in team1_file:
		print(row.split(',')[3])'''