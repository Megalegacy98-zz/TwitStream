# -*- coding: utf-8 -*-

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import codecs
import time
from timeit import default_timer

start = default_timer()

ckey = ''
csecret = ''
atoken = ''
asecret = ''

i = 0
j = 0

test = input("What do you want to stream tweets from? > ")
test3 = input("What do you want the file to be named? > ")
test2 = input("And for how many minutes? > ")

test2 = int(test2)

test2 = int(test2) * 60

class listener(StreamListener):
        
	def on_status(self, status):
		global test2
		global test3
		global start
		global i
		duration = default_timer() - start
		if  duration <= int(test2):
			try:
					
				def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
					enc = file.encoding
					if enc == 'UTF-8':
						print(*objects, sep=sep, end=end, file=file)
					else:
						f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
						print(*map(f, objects), sep=sep, end=end, file=file)

				uprint(u""+status.text)
				save = open(test3+'.txt', 'a')
				save.write(status.text)
				save.write('\n')
				save.write('\n')
				save.close()
				return True
		
			i+=1
							
							
			except BaseException as e:
					pass
					
			else:
				global j
				j = i/test2
				x = open(test3+".txt","r")

				
				print("\nDone!", end="\n")
				print("There were "+str(i)+" tweets\n")
				print(str(j)+" per second")
				x.close()
				y = open(test3+".txt", "a")
				y.write("\nREPORT:\n"+str(i)+" tweets\n"+str(j)+" tweets a second")
				y.close()
				exit()

	def on_error(self,status):
		print(status)
		
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth=auth, listener=listener())
twitterStream.filter(track=[test])
