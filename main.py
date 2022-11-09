from bs4 import BeautifulSoup
import requests

with open('./home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_="card-body")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split(' ')[-1]
    

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
total_jobs = soup.find('span', id='totolResultCountsId').text
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
count = 0
finished = False
unfamiliar_skills = []
while finished == False:
    unfamiliar_skills.append(input('Unfamiliar skill:'))
    ask_again = input('Do you want to add another one? (Y/N)')
    if ask_again.lower() == "y":
        finished = False
    else:
        finished = True
    
for job in jobs:
    publish_date = job.find('span', class_="sim-posted").span.text
    skills = job.find('span', class_="srp-skills").text.replace(' ', '')
    
    if 'few' not in publish_date:
        continue

    hasUnfamiliarSkill = False
    for skill in unfamiliar_skills:
        if skill in skills:
            hasUnfamiliarSkill = True
    
    if hasUnfamiliarSkill == True:
        continue

    job_title = job.find('h2').text
    company_name = job.find('h3').text.replace(' ', '')
    more_info = job.header.h2.a['href']

    print(f'Title: {job_title.strip()}') 
    print(f'More info: {more_info}') 
    print(f'Company: {company_name.strip()}')
    print(f'Skills: {skills.strip()}')
    print(f'Published: {publish_date.strip()}')
    print('---------------------------')

    count += 1

print(count)