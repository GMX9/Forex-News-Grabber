#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import requests
import bs4
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class Get:
	def generateUserAgent(self):
		software_names = [SoftwareName.CHROME.value]
		operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

		user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

		# Get list of user agents.
		user_agents = user_agent_rotator.get_user_agents()

		# Get Random User Agent String.
		user_agent = user_agent_rotator.get_random_user_agent()
		return(user_agent)         

	# Iterate items from news
	def allNews(self,website):
		r = requests.post(website)
		response = r.text
		html = bs4.BeautifulSoup(response, 'lxml')
		divs = html.findAll(class_='fxBgNext')
		for div in divs:
			try:
				print(div.find('a')['href'])
				print(div.find('a').contents[0])
			except:
				print("Não foi possível obter os dados.")

	def singleNew(self,link):
		user_agent = self.generateUserAgent()
		r = requests.get(website, headers = {'User-agent': user_agent})
		response = r.text
		html = bs4.BeautifulSoup(response, 'lxml')
		divs = html.find(class_='contentflex__noposition')
		try:
			print(divs)
			#print(div.find('p').contents[0])
		except:
			print("Não foi possível obter os dados.")

	def saveToDB(title,link):
		try:
			connection = mysql.connector.connect(host='localhost',
												 database='Electronics',
												 user='pynative',
												 password='pynative@#29')

			cursor = connection.cursor()
			query = """INSERT INTO posts_tg_pt (title,link,description,status,featured,views) 
									VALUES (%s, %s, %s, %s, %s, %s, %s) """
			empty = ""                        
			recordTuple = (title, link, empty, 0, 0, 0)
			cursor.execute(query, recordTuple)
			connection.commit()
			print("[+] Record inserted successfully.")

		except mysql.connector.Error as error:
			print("[-] Failed to insert into MySQL table {}".format(error))

		finally:
			if (connection.is_connected()):
				cursor.close()
				connection.close()
				print("[+] MySQL connection is closed")


algo = Get()
website = 'https://www.instaforex.eu/pt/forex-news'
#algo.allNews(website)
#algo.singleNew(new)

			
