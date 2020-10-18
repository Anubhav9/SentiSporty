import flask
import requests
from flask import Flask,render_template,request
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import date



app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def index():
	today = date.today()
	d2 = today.strftime("%B %d, %Y")
	response=requests.get('http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=fbaea266b04d4c3d914e62557883e5c5')
	a=response.json()
	analyser = SentimentIntensityAnalyzer()
	
	text_1=a['articles'][0]['title']
	text_1_author=a['articles'][0]['source']['name']
	text_1_score=analyser.polarity_scores(text_1)
	score_1=text_1_score['compound']
	if(score_1>=0.05):
		result_1='Positive'
	elif(score_1<0.05 and score_1>=-0.05):
		result_1='Neutral'
	else:
		result_1='Negative'
	text_1_link=a['articles'][0]['url']

	text_2=a['articles'][1]['title']
	text_2_author=a['articles'][1]['source']['name']
	text_2_score=analyser.polarity_scores(text_2)
	score_2=text_2_score['compound']
	if(score_2>=0.05):
		result_2='Positive'
	elif(score_2<0.05 and score_2>=-0.05):
		result_2='Neutral'
	else:
		result_2='Negative'
	text_2_link=a['articles'][1]['url']

	text_3=a['articles'][2]['title']
	text_3_author=a['articles'][2]['source']['name']
	text_3_score=analyser.polarity_scores(text_3)
	score_3=text_3_score['compound']
	if(score_3>=0.05):
		result_3='Positive'
	elif(score_3<0.05 and score_3>=-0.05):
		result_3='Neutral'
	else:
		result_3='Negative'
	text_3_link=a['articles'][2]['url']

	text_4=a['articles'][3]['title']
	text_4_author=a['articles'][3]['source']['name']
	text_4_score=analyser.polarity_scores(text_4)
	score_4=text_4_score['compound']
	if(score_4>=0.05):
		result_4='Positive'
	elif(score_4<0.05 and score_4>=-0.05):
		result_4='Neutral'
	else:
		result_4='Negative'
	text_4_link=a['articles'][3]['url']

	text_5=a['articles'][4]['title']
	text_5_author=a['articles'][4]['source']['name']
	text_5_score=analyser.polarity_scores(text_5)
	score_5=text_5_score['compound']
	if(score_5>=0.05):
		result_5='Positive'
	elif(score_5<0.05 and score_5>=-0.05):
		result_5='Neutral'
	else:
		result_5='Negative'
	text_5_link=a['articles'][4]['url']

	text_6=a['articles'][5]['title']
	text_6_author=a['articles'][5]['source']['name']
	text_6_score=analyser.polarity_scores(text_6)
	score_6=text_6_score['compound']
	if(score_6>=0.05):
		result_6='Positive'
	elif(score_6<0.05 and score_6>=-0.05):
		result_6='Neutral'
	else:
		result_6='Negative'
	text_6_link=a['articles'][5]['url']

	text_7=a['articles'][6]['title']
	text_7_author=a['articles'][6]['source']['name']
	text_7_score=analyser.polarity_scores(text_7)
	score_7=text_7_score['compound']
	if(score_7>=0.05):
		result_7='Positive'
	elif(score_7<0.05 and score_7>=-0.05):
		result_7='Neutral'
	else:
		result_7='Negative'
	text_7_link=a['articles'][6]['url']

	text_8=a['articles'][7]['title']
	text_8_author=a['articles'][7]['source']['name']
	text_8_score=analyser.polarity_scores(text_8)
	score_8=text_8_score['compound']
	if(score_8>=0.05):
		result_8='Positive'
	elif(score_8<0.05 and score_8>=-0.05):
		result_8='Neutral'
	else:
		result_8='Negative'
	text_8_link=a['articles'][7]['url']

	text_9=a['articles'][8]['title']
	text_9_author=a['articles'][8]['source']['name']
	text_9_score=analyser.polarity_scores(text_9)
	score_9=text_9_score['compound']
	if(score_9>=0.05):
		result_9='Positive'
	elif(score_9<0.05 and score_9>=-0.05):
		result_9='Neutral'
	else:
		result_9='Negative'
	text_9_link=a['articles'][8]['url']


	text_10=a['articles'][9]['title']
	text_10_author=a['articles'][9]['source']['name']
	text_10_score=analyser.polarity_scores(text_10)
	score_10=text_10_score['compound']
	if(score_10>=0.05):
		result_10='Positive'
	elif(score_10<0.05 and score_10>=-0.05):
		result_10='Neutral'
	else:
		result_10='Negative'
	text_10_link=a['articles'][9]['url']


	text_11=a['articles'][10]['title']
	text_11_author=a['articles'][10]['source']['name']
	text_11_score=analyser.polarity_scores(text_11)
	score_11=text_11_score['compound']
	if(score_11>=0.05):
		result_11='Positive'
	elif(score_11<0.05 and score_11>=-0.05):
		result_11='Neutral'
	else:
		result_11='Negative'
	text_11_link=a['articles'][10]['url']

	text_12=a['articles'][11]['title']
	text_12_author=a['articles'][11]['source']['name']
	text_12_score=analyser.polarity_scores(text_12)
	score_12=text_12_score['compound']
	if(score_12>=0.05):
		result_12='Positive'
	elif(score_12<0.05 and score_12>=-0.05):
		result_12='Neutral'
	else:
		result_12='Negative'
	text_12_link=a['articles'][11]['url']


	text_13=a['articles'][12]['title']
	text_13_author=a['articles'][12]['source']['name']
	text_13_score=analyser.polarity_scores(text_13)
	score_13=text_13_score['compound']
	if(score_13>=0.05):
		result_13='Positive'
	elif(score_13<0.05 and score_13>=-0.05):
		result_13='Neutral'
	else:
		result_13='Negative'
	text_13_link=a['articles'][12]['url']

	text_14=a['articles'][13]['title']
	text_14_author=a['articles'][13]['author']
	text_14_score=analyser.polarity_scores(text_14)
	score_14=text_14_score['compound']
	if(score_14>=0.05):
		result_14='Positive'
	elif(score_14<0.05 and score_14>=-0.05):
		result_14='Neutral'
	else:
		result_14='Negative'
	text_14_link=a['articles'][13]['url']

	text_15=a['articles'][14]['title']
	text_15_author=a['articles'][14]['author']
	text_15_score=analyser.polarity_scores(text_15)
	score_15=text_15_score['compound']
	if(score_15>=0.05):
		result_15='Positive'
	elif(score_15<0.05 and score_15>=-0.05):
		result_15='Neutral'
	else:
		result_15='Negative'
	text_15_link=a['articles'][14]['url']


	text_16=a['articles'][15]['title']
	text_16_author=a['articles'][15]['author']
	text_16_score=analyser.polarity_scores(text_16)
	score_16=text_16_score['compound']
	if(score_16>=0.05):
		result_16='Positive'
	elif(score_16<0.05 and score_16>=-0.05):
		result_16='Neutral'
	else:
		result_16='Negative'
	text_16_link=a['articles'][15]['url']


	text_17=a['articles'][16]['title']
	text_17_author=a['articles'][16]['author']
	text_17_score=analyser.polarity_scores(text_17)
	score_17=text_17_score['compound']
	if(score_17>=0.05):
		result_17='Positive'
	elif(score_17<0.05 and score_17>=-0.05):
		result_17='Neutral'
	else:
		result_17='Negative'
	text_17_link=a['articles'][16]['url']


	text_18=a['articles'][17]['title']
	text_18_author=a['articles'][17]['author']
	text_18_score=analyser.polarity_scores(text_18)
	score_18=text_18_score['compound']
	if(score_18>=0.05):
		result_18='Positive'
	elif(score_18<0.05 and score_18>=-0.05):
		result_18='Neutral'
	else:
		result_18='Negative'
	text_18_link=a['articles'][17]['url']


	text_19=a['articles'][18]['title']
	text_19_author=a['articles'][18]['author']
	text_19_score=analyser.polarity_scores(text_19)
	score_19=text_19_score['compound']
	text_19_link=a['articles'][18]['url']


	text_20=a['articles'][19]['title']
	text_20_author=a['articles'][19]['author']
	text_20_score=analyser.polarity_scores(text_20)
	score_20=text_20_score['compound']
	text_20_link=a['articles'][19]['url']


	return render_template('index.html',t_1_a=text_1_author,t_1=text_1,t_2_a=text_2_author,t_2=text_2,
		t_3_a=text_3_author,t_3=text_3,t_4_a=text_4_author,t_4=text_4,t_5_a=text_5_author,t_5=text_5,t_6_a=text_6_author,
		t_6=text_6,t_7_a=text_7_author,t_7=text_7,t_8_a=text_8_author,t_8=text_8,t_9_a=text_9_author,t_9=text_9,t_10_a=text_10_author,
		t_10=text_10,t_11_a=text_11_author,t_11=text_11,t_12_a=text_12_author,t_12=text_12,
		t_13_a=text_13_author,t_13=text_13,t_14_a=text_14_author,t_14=text_14,t_15_a=text_15_author,
		t_15=text_15,t_16_a=text_16_author,t_16=text_16,t_17_a=text_17_author,t_17=text_17,text_18_a=text_18_author,
		t_18=text_18,t_19_a=text_19_author,t_19=text_19,t_20_a=text_20_author,t_20=text_20,
		a=result_1,b=result_2,c=result_3,d=result_4,e=result_5,f=result_6,g=result_7,h=result_8,
		i=result_9,j=result_10,k=result_11,l=result_12,m=result_13,n=result_14,o=result_15,
		p=result_16,q=result_17,r=result_18,t_1_l=text_1_link,t_2_l=text_2_link,
		t_3_l=text_3_link,t_4_l=text_4_link,t_5_l=text_5_link,t_6_l=text_6_link,
		t_7_l=text_7_link,t_8_l=text_8_link,t_9_l=text_9_link,t_10_l=text_10_link,
		t_11_l=text_11_link,t_12_l=text_12_link,t_13_l=text_13_link,t_14_l=text_14_link,
		t_15_l=text_15_link,t_16_l=text_16_link,t_17_l=text_17_link,t_18_l=text_18_link,
		t_19_l=text_19_link,t_20_l=text_20_link,datei=d2)

if __name__ == '__main__':
    app.run(debug=True)




