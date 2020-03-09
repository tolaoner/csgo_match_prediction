#def scrape_team_data(team_name):
from selenium import webdriver
browser=webdriver.Chrome(r"C:\chromedriver.exe")
browser.get('https://www.hltv.org/stats/teams?startDate=2019-09-08&endDate=2020-03-08')
browser.find_element_by_xpath("""/html/body/div[2]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/a""").click()
stats=browser.find_elements_by_class_name('stats-top-menu-item.stats-top-menu-item-link')
stats[1].click()
maps=browser.find_elements_by_class_name('statsMapPlayed')
results=browser.find_elements_by_class_name('text-center')
table=browser.find_element_by_tag_name('tbody')
rows=table.find_elements_by_tag_name('tr')
data=[]
match=[]
for row in rows:
    cols=row.find_elements_by_tag_name('td')
    for j in range(7):
        match.append(cols[j].text)
    data.append(match)
print(len(data))
#print(data)
