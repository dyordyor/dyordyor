import openpyxl
from openpyxl import load_workbook
import os
import openai


api_key = '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'
openai.api_key = api_key
filenames = os.listdir('./')

for file in filenames:
	if file[-5:] == '.xlsx':
		filenames = file
		print(file)
		break

wb = load_workbook(file)    
sheet = wb['words_count']

def write_chatgpt(text):

	response = openai.Completion.create(
		engine = 'text-davinci-003',
		prompt = text,
		top_p = 1,
		temperature = 0.4,
		max_tokens = 2000,
		)
	return response.choices[0].text

word_list = []
numb_list = []
counter = 2
while True:
	word = sheet[f'A{counter}'].value
	numb = sheet[f'B{counter}'].value
	if word == None:
		break
	else:
		numb_list.append(numb)
		word_list.append(word)
		counter+=1	
print(word_list)
word_prompt = """Write a "+" sign next to words related to cryptocurrency that specifically and uniquely refer to particular tokens, platforms, or technologies (examples: BTC, Eth, Ethereum, Arbitrum, Doge, NFT, etc.). Please DO NOT add a "+" sign next to generic words, even if they are related to cryptocurrency or could be used in a broad sense (examples: token, game, mint, app, asset, address, network, contract, platform, chain, collection, etc.). Write a "-" sign next to words that don't fit the criteria.

Example:
like, -
money, -
Ethereum, +
leverage, -
BTC, +:
"""

true_words = []
counter = 2
encounter = 1
countsdad = 11
for count in range((len(word_list) // 250) + 1):
	words_with_plus = []
	exmpl = ''
	sex_exmpl = ''
	for i in range(250):
		try:
			exmpl = exmpl + f'{word_list[counter]}' + ', ' + '\n'
			counter+=1
		except Exception:
			break	
	try:
		answer = write_chatgpt(f'{word_prompt}\n{exmpl}\n')
	except:
		write_chatgpt(f'forget all what i wrote')
		answer = write_chatgpt(f'{word_prompt}\n{exmpl}\n')
	print(f'{word_prompt}\n{exmpl}\n')
	print(answer)
	print('//////////////////')
	for line in answer.split(sep='\n'):
		try:
			if '+' in line:
				words_with_plus.append(line)
		except Exception:
			pass

	for word in words_with_plus:
		word = word.replace(',', '')
		word = word.replace('+', '')
		word = word.replace(' ', '')

		sex_exmpl = sex_exmpl + f'{word}' +', ' + '\n'
	try:	
		second_led = write_chatgpt(f'{word_prompt}\n"{sex_exmpl}"\n')
	except:
		write_chatgpt(f'forget all what i wrote')
		second_led = write_chatgpt(f'{word_prompt}\n"{sex_exmpl}"\n')

	#print(f'{word_prompt}\n{sex_exmpl}\n')
	print(f'{word_prompt}\n"{sex_exmpl}"\n')
	print(second_led)
	if len(second_led.split('\n')) == 1:
		for lines in second_led.split(' '):
			if '+' in lines:
				lines = lines.replace(',', '')
				lines = lines.replace('+', '')
				lines = lines.replace(' ', '')
				lines = lines.lower()
				if lines not in true_words:
					true_words.append(lines)
					sheet[f'D{encounter}'].value = lines
					if lines not in word_list:
						sheet[f'E{encounter}'].value = 'er'
					else:
						sheet[f'E{encounter}'].value = numb_list[word_list.index(lines)]
						countsdad = int(numb_list[word_list.index(lines)])
					encounter+=1
		
	else:
		for lines in second_led.split('\n'):
			if '+' in lines:
				lines = lines.replace(',', '')
				lines = lines.replace('+', '')
				lines = lines.replace(' ', '')
				lines = lines.lower()
				if lines not in true_words:
					true_words.append(lines)
					sheet[f'D{encounter}'].value = lines
					if lines not in word_list:
						sheet[f'E{encounter}'].value = 'er'
					else:
						
						sheet[f'E{encounter}'].value = numb_list[word_list.index(lines)]
						countsdad = int(numb_list[word_list.index(lines)])
					encounter+=1
	print(countsdad)				
	if countsdad < 10:
		break			
	print(true_words)
wb.save('result.xlsx')

