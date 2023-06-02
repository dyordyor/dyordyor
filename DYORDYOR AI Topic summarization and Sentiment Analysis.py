from __future__ import print_function
import os.path
import pickle
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class GoogleSheet():
	SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
	service = None

	def __init__(self):
		creds = None
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				creds = pickle.load(token)

		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				print('flow')
				flow = InstalledAppFlow.from_client_secrets_file(
					'credentials.json', self.SCOPES)
				creds = flow.run_local_server(port=0)
			with open('token.pickle', 'wb') as token:
				pickle.dump(creds, token)

		self.service = build('sheets', 'v4', credentials=creds)

	def updateRangeValues(self, range, values, idsh):
		data = [{
			'range': range,
			'values': values
		}]
		body = {
			'valueInputOption': 'USER_ENTERED',
			'data': data
		}
		result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=idsh, body=body).execute()
		print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

	def getRangeValues(self, range, idsh):
		resp = self.service.spreadsheets().values().get(spreadsheetId=idsh, range=range).execute()
		return resp    


def main():
	spreadsheetsss = input("Введите айди таблицы: ")
	gs = GoogleSheet()
	counter = 2
	test_range = 'words_count!A2:A99999'


	category = []
	#gs.updateRangeValues(test_range, test_values)
	diap = {}


	for i in gs.getRangeValues(test_range, spreadsheetsss)['values']:
		for b in i:
			category.append(b)

	test_range = 'Лист1!I2:I99999'
	tag_list = []

	for i in gs.getRangeValues(test_range, spreadsheetsss)['values']:
		for b in i:
			tag_list.append(b.replace("'", ""))
	for_key = []
	i = 2
	for cut in category:
		for tag in tag_list:
			if cut.lower() in tag.lower():
				for a in tag.lower().split():
					if a == cut:
						for_key.append(i) #Столб I
						break

			i+=1
		diap.update({cut : for_key})
		for_key = []
		i = 2	
	i = 2
	second = 2
	catcounter = 2
	z = []
	for ssss in range (99999):
		z.append([' '])
	print('lol')	
	gs.updateRangeValues(f'Лист2!Z1:Z99999',  z, spreadsheetsss)
	for sad in category:
		final_tweets = []
		numbs = diap.get(sad)
		start = i
		for numb in numbs:

			#gs.updateRangeValues(f'Лист2!M{i}:N{i}',  [[f'=Лист1!B{numb}',f'=Лист1!C{numb}']])  #gs.getRangeValues(f'Лист1!B{numb}:C{numb}')['values'])
			#gs.updateRangeValues(f'Лист2!M{i}', [['=Лист1!C2']])
			final_tweets.append([f'=Лист1!B{numb}',f'=Лист1!C{numb}'])
			i+=1
		print(sad)	
		print(final_tweets)
		if numbs == [] and len(numbs) < 45:
			gs.updateRangeValues(f'Лист2!A{catcounter}:C{catcounter}',  [[sad, 'None', 'None']], spreadsheetsss)  #gs.getRangeValues(f'Лист1!B{numb}:C{numb}')['values'])
			catcounter+=1

		elif len(final_tweets) > 45:
			second = catcounter
			n = 0
			b = i
			s = 0
			f = 0

			for count in range((len(final_tweets) // 45) + 1):
				test_list = []
				for s in range(45):
					try:
						test_list.append(final_tweets[n])
						n+=1
					except Exception:
						break	

				

				print(f'Лист2!T{(b - len(final_tweets)) + len(test_list)}:U{(b - len(final_tweets)) + (len(test_list) + len(test_list))}')

				#first = b - len(final_tweets)
				#last = i
				#
				#
				#


				gs.updateRangeValues(f'Лист2!T{(b - len(final_tweets)) + len(test_list)}:U{(b - len(final_tweets)) + len(test_list) + len(test_list)}', test_list, spreadsheetsss)
				gs.updateRangeValues(f'Лист2!Q{second}',  [[f"Write a short concise news report on what is being said about {sad} based on the following. It's mandatory to quote key statements directly and provide twitter handles"]], spreadsheetsss)
				gs.updateRangeValues(f'Лист2!R{second}',  [[f'=GPT(Q{second};T{(b - len(final_tweets)) + len(test_list)}:U{(b - len(final_tweets)) + len(test_list) + len(test_list)})']], spreadsheetsss)	
				b += len(test_list)	
				second+=1
				time.sleep(2)
			hanfler = f"Write a short concise news report on what is being said about {sad} based on the following. It's mandatory to quote key statements directly and provide twitter handles"
			gs.updateRangeValues(f'Лист2!Y{catcounter}',  [[hanfler]], spreadsheetsss)

			if (len(final_tweets) // 50) + 1 > 50:
				pass

			gs.updateRangeValues(f'Лист2!A{catcounter}:C{catcounter}',  [[sad, f'=GPT(Y{catcounter};R{catcounter}:U{catcounter + (len(final_tweets) // 50) + 1})', f'=GPT("Please measure the general sentiment on {sad} in this dataset. Is it Neutral, bearish, or bullish? Pick one of these three.";R{catcounter}:U{catcounter + (len(final_tweets) // 50) + 1})']], spreadsheetsss)  #gs.getRangeValues(f'Лист1!B{numb}:C{numb}')['values'])
			catcounter+=1





		else:	
			gs.updateRangeValues(f'Лист2!M{start}:N{i}', final_tweets, spreadsheetsss)	
			#Write a short concise news report on what is being said about AMP based on the following. It's mandatory to quote key statements directly and provide twitter handles
			#Please measure the general sentiment on CATEGORY NAME in this dataset. Is it Neutral, bearish, or bullish? Pick one of these three.
			gs.updateRangeValues(f'Лист2!O{catcounter}',  [[f"Write a short concise news report on what is being said about {sad} based on the following. It's mandatory to quote key statements directly and provide twitter handles"]], spreadsheetsss)
			gs.updateRangeValues(f'Лист2!A{catcounter}:C{catcounter}',  [[sad, f'=GPT(O{catcounter};M{start}:N{i})', f'=GPT("Please measure the general sentiment on {sad} in this dataset. Is it Neutral, bearish, or bullish? Pick one of these three.";M{start}:N{i})']], spreadsheetsss)  #gs.getRangeValues(f'Лист1!B{numb}:C{numb}')['values'])
			catcounter+=1

		#i+=len(diap.get(sad))
		time.sleep(3)

if __name__ == '__main__':
	main()
