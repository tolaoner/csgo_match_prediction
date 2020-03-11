def scrape_team_data(team_name,bool_json):
    #put the name of the team you want the stats of.'str'. Put in true for json file, false for csv file.
	from selenium import webdriver
	import write_to_json
	import csv
	browser=webdriver.Chrome(r"C:\chromedriver.exe")
	browser.get('https://www.hltv.org/stats/teams?startDate=2019-09-08&endDate=2020-03-08')
	#teams_table=browser.find_elements_by_tag_name('tbody')
	#teams=teams_table.find_elements_by_tag_name('tr')
	browser.find_element_by_link_text(team_name).click()
	stats=browser.find_elements_by_class_name('stats-top-menu-item.stats-top-menu-item-link')
	stats[1].click()
	#maps=browser.find_elements_by_class_name('statsMapPlayed')
	#results=browser.find_elements_by_class_name('text-center')
	table=browser.find_element_by_tag_name('tbody')
	rows=table.find_elements_by_tag_name('tr')
	data=[]
	date=[]
	opponent=[]
	score=[]
	maps=[]
	win_lose=[]
	for row in rows:
		cols=row.find_elements_by_tag_name('td')
		date.append(cols[0].text)
		score.append(cols[5].text)
		maps.append(cols[4].text)
		opponent.append(cols[3].text)
		win_lose.append(cols[6].text)
	data=list(zip(date,opponent,maps,score,win_lose))
	'''print(data)
	print(score)
	print(maps)
	print(opponent)
	print(win_lose)'''
	if bool_json:
		write_to_json.write_json(team_name,data)
	else:
		with open(f'{team_name}.csv','w', newline='') as csv_file:
			wr=csv.writer(csv_file)
			wr.writerows(data)
#scrape_team_data('INTZ',False)
'''scrape_team_data('Natus Vincere',False)
scrape_team_data('Astralis',False)
scrape_team_data('FaZe',False)
scrape_team_data('TYLOO',False)
scrape_team_data('Liquid',False)
scrape_team_data('G2',False)'''	
#scrape_team_data('FURIA',False)
#scrape_team_data('ATK',False)
#scrape_team_data('ViCi',False)
#scrape_team_data('MIBR',False)
#scrape_team_data('mousesports',False)
'''scrape_team_data('AVANGAR',False)
scrape_team_data('Heroic',False)'''
#scrape_team_data('Virtus.pro',False)
#scrape_team_data('HellRaisers',False)
'''scrape_team_data('BIG',False)
scrape_team_data('NiP',False)
scrape_team_data('fnatic',False)
scrape_team_data('EHOME',False)
scrape_team_data('Winstrike',False)
scrape_team_data('eUnited',False)
scrape_team_data('Evil Geniuses',False)'''
