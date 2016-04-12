from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from collections import Counter
import twitter


def base(request):
	return render_to_response('base.html', context_instance = RequestContext(request))

def help(request):
	return render_to_response('help.html')

def about(request):
	return render_to_response('about.html')
   
def lexical_diversity(tokens):
	lexDiv =  100.0*len(set(tokens))/len(tokens)
	lexDiv = round(lexDiv, 2)
	return lexDiv

def average_words(statuses):
	total_words = sum([ len(s.split()) for s in statuses ])
	return 1.0*total_words/len(statuses)

def search_result(request):
	varHashtag = request.POST.get('hashtag')
	count = 100
	CONSUMER_KEY = 'P8TbqI93uitIPB2ie275GP0D8'
	CONSUMER_SECRET = 'rUv8Lc2bw5CRiQzXB9FPcHKSBCpoNWpSVSNbMwFqRGIVLjz1CY'
	OAUTH_TOKEN = '82629030-RALOevVc0oCOe0kVtBx09ChwfKg6UQ3v2uiTBD1rU'
	OAUTH_TOKEN_SECRET = 'PzUdiqtBUfXjGum2bX0uHvFRaHUGsxYDUjGrqYgncPED1'
	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)

	# See https://dev.twitter.com/docs/api/1.1/get/search/twseets
	search_results = twitter_api.search.tweets(q=varHashtag, count=count)
	statuses = search_results['statuses']
	
	retweets = [
		# Store out a tuple of these three values ...
		(status['retweet_count'],
		status['retweeted_status']['user']['screen_name'],
		status['text'])
		
		# ... for each status ...
		for status in statuses
		# ... so long as the status meets this condition.
			if status.has_key('retweeted_status')
	]

	status_texts = [ status['text']
		for status in statuses ]

	screen_names = [ user_mention['screen_name']
		for status in statuses
			for user_mention in status['entities']['user_mentions'] ]

	hashtags = [ hashtag['text']
		for status in statuses
			for hashtag in status['entities']['hashtags'] ]

		# Compute a collection of all words from all tweets
	words = [ w for t in status_texts 
					for w in t.split() ]

	word = lexical_diversity(words)
	scrNames = lexical_diversity(screen_names)
	hstg = lexical_diversity(hashtags)
	avgText =  average_words(status_texts)
	

	retweets = sorted(retweets,reverse = True) 

	return render_to_response('search_result.html',{'judul':varHashtag,'rt':retweets, 
		'word': word, 'scrNames': scrNames, 'hstg':hstg, 'avgText':avgText})