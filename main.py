from bs4 import BeautifulSoup
import requests
import time

with open('./home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_="card-body")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split(' ')[-1]
    

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    total_jobs = soup.find('span', id='totolResultCountsId').text
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    count = 0
    finished = False
    unfamiliar_skills = []
    while finished == False:
        message = 'an unfamiliar skill' if len(unfamiliar_skills) == 0 else 'another one'
        answer = input(f'Do you want to add {message}? (Y/N)')
        if answer.lower() == "y":
            finished = False
            unfamiliar_skills.append(input('Unfamiliar skill:'))
        else:
            finished = True
        # ask = input('Do you want to add another one? (Y/N)')
        
    for index, job in enumerate(jobs):
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

        with open(f'posts/{index}.txt', 'w') as file:
            file.write(f'Title: {job_title.strip()} \n') 
            file.write(f'More info: {more_info} \n') 
            file.write(f'Company: {company_name.strip()} \n')
            file.write(f'Skills: {skills.strip()} \n')
            file.write(f'Published: {publish_date.strip()}')
 
        count += 1

    print(count)

if __name__ == '__main__':
    while True:
        find_jobs()
        print('Waiting...')
        time.sleep(60 * 10)