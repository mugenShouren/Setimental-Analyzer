import json
import random

data = []
file_name = 'Electronics_5'
with open(f'D://++PROJECT++//NLP//{file_name}.json') as f:
	for line in f:
		review = json.loads(line)
		year = int(review['reviewTime'].split(' ')[-1])
		if year == 2014 or year == 2015:
			data.append(review)

final_data = random.sample(data, 100000)


with open(f'D://++PROJECT++//NLP//Electronics_small.json', 'w') as f:
	for review in final_data:
		f.write(json.dumps(review)+'\n')