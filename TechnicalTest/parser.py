import glob
import os
import json
from datetime import datetime , date
import pandas as pd

#To-Do : create a dynamic variable to understand nationality using mobile country code
nationality={'+1':'American'}



def read_files(source):
	'''Returns list of all file path present treating current path as parent'''
	path ='.'
	files = [f for f in glob.glob(source+"/*.json", recursive=True)]
	#Sort files according to source
	return files;

def cal_age(birthDate):
	'''Returns age in years and taking Date of Birth as input eg. 18 Nov 1889'''
	date_time_obj = datetime.strptime(birthDate,'%d %b %Y')
	today=date.today()
	age=today.year-date_time_obj.year-((today.month,today.day)<(date_time_obj.month, date_time_obj.day))
	return age

def parser(filePath):
	'''Returns parsed json from multiple files as a dictionary
	
	Parameters
    ----------
    filePath:str
    	File path is realtive path of file
	'''
	temp_dist={}
	with open(filePath) as f:
		data = json.load(f)

	#print("\nJSON String {}".format(data))

	try:
		#concatinate name
		temp_dist['name'] = data['name']['first_name'] +" "+data['name']['last_name']
	except Exception as e:
		temp_dist['name']=data['name']

	#crawl mobile number and country code
	if len(data['mobile'])>10:
		temp_dist['mobile']=data['mobile'][-10:]
		temp_dist['mobile_country_code']=data['mobile'][:(len(data['mobile'])-10)]
	else:
		temp_dist['mobile'] =data['mobile']
		temp_dist['mobile_country_code']=data['mobile_country_code']
		
	try:
		temp_dist['age']=cal_age(data['dob'])
	except Exception as e:
		YMD_list=data['age'].split(' ')
		temp_dist['age']= YMD_list[0].replace('y','')

	try:
		temp_dist['nationality']=data['nationality']
	except Exception as e:
		temp_dist['nationality']=nationality[data['mobile_country_code']]

	return temp_dist	

if __name__=='__main__':
	df=pd.DataFrame()
	for JsonFilePath in read_files("**"):
		#print ("\nParsed Json {}".format(parser(JsonFilePath)))
		df = df.append(parser(JsonFilePath), ignore_index=True)

	print(df)
	print("\n\n")
	print(df[df.age == '29'])
	print("\n\n")
	df.to_csv('test.csv')
	