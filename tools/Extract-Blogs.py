import requests, os
from bs4 import BeautifulSoup
from colorama import Fore, Style
#from git import Repo

root_url = 'https://www.dbi-services.com/blog/'
author_url = root_url + 'author/ols/'
dest_path = 'content/posts/'

def determineTags(title):
	tagsList = ['kafka','zabbix','monitoring','dynatrace','ansible']
	tags = ['dbi-services']
	for t in tagsList:
		if t in title:
			tags.append(t)
	return tags

def getBlogs(url,destination):
	currentPage = 1
	blogsCount = 0

	nextpage = True
	while nextpage:
		
		currentUrl = url + str(currentPage) + '/'
		response = requests.get(currentUrl)
		if response.status_code == 404:
			print(f'\n {currentPage-1} pages processed.')
			return 0
		print(f'\nProcessing page {currentPage}')
		html_text = response.text
		soup = BeautifulSoup(html_text,'html.parser')

		link = ''
		for article in soup.find_all('article'):
			# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
			# print(article)
			# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
			
			title = article.h2.text.strip()
			
			summary = article.p.text
			
			# link = article.find_all('a')[1]['href']
			link = article.h2.parent.attrs['href'] 

			sanitized_title = link.replace(root_url,'').replace('/','')

			tags = determineTags(sanitized_title)

			publishedDateStr = article.find('div',class_='infos').text.split(' ')[0]
			publishedDateArray = publishedDateStr.split('.')
			publishedDate = f'{publishedDateArray[2]}-{publishedDateArray[1]}-{publishedDateArray[0]}'
			pubDateStr = str(publishedDate)
			pubDateStr = pubDateStr.split()[0]

			# Prepare string to write in file
			buildStr = '---\n'
			buildStr += f'title: "{ title }"\n'
			buildStr += f'date: { pubDateStr }\n'
			buildStr += f'tags: {tags}\n'
			# buildStr += f'params:\n'
			# buildStr += f'  dbiblogtitle: { sanitized_title }\n'
			# buildStr += 'author : "Olivier Spiesser"\n'
			buildStr += '---\n'
			buildStr += summary

			with open(destination + sanitized_title + '.md', "w", encoding='utf-8') as fp:
				fp.write(buildStr)
				blogsCount += 1
			# try:
			# 	path.write_text(buildStr)
			# except:
			# 	print(buildStr)
			# 	exit(1)
			print(f'{sanitized_title} {Fore.GREEN}written{Fore.RESET}.')
				
		currentPage += 1
	return blogsCount

#########

if __name__ == "__main__":
	#path_exists = Path.exists(dest_path)
	path_exists = True
	if path_exists:
		print('Destination path: ' + dest_path)
		page_url = author_url + 'page/'
		#print(page_url)
		newBlogsCount = getBlogs(page_url,dest_path)
	else:
		print(f'Path {dest_path} does not exist!')

print(f'{newBlogsCount} new blog(s) found.')

# newBlogsCount = 1 ## fake
if (newBlogsCount > 0):
	print('Calling hugo: ', end='', flush=True)
	stream = os.popen('hugo')
	hugoOutput = stream.read()
	print(Fore.GREEN + 'OK' + Style.RESET_ALL)

	# Add files to git
	# print('Initiating git repo object')
	# repo = Repo('.')
	# print('Add files to repo')
	# repo.index.add('content')