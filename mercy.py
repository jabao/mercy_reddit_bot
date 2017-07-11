import praw
import time
import sys
import os

user = 'heyguysimainmercy'
subreddit = 'bottestingsite'
num_replies = 0
#how many comments to scan per run
comment_limit = 100
#strings to scan for
strings = ['mercy main', 'main mercy', 'mercy player', 'plays mercy']

def main():
	#log in
	print('logging in', file=sys.stderr)
	reddit = praw.Reddit('bot1')
	print('logged in', file.sys.stderr)
	#subreddit to scan
	sub = reddit.subreddit(subreddit)
	#comments replied to
	replies = get_replies()

	delete(reddit)
	while(True):
		run(reddit, sub, replies)
		print('sleeping 10s', file=sys.stderr)
		print('total replies: ' + str(num_replies), file=sys.stderr)
		print(replies, file=sys.stderr)
		time.sleep(10)

def run(r, sub, replies):
	"""This function runs the bot
	Params: 
	r - reddit instance
	sub - subreddit the bot scans for comments"""
	ok = False
	comments = sub.comments(limit=comment_limit)
	#loop through comments to search for matching text
	for comment in comments:
		for rep in comment.replies: # testing reply detection
			print(reply.body, file=sys.stderr)
		for string in strings:
			if string in comment.body.lower():
				#do not reply if already replied (this implementation broken)
				'''for rep in comment.replies:
					print('testerdogger', file=sys.stderr)
					if rep.author == r.user.me():
						print('already replied', file=sys.stderr)
						ok = True
						break'''
				#reply if not to self and do not reply if already replied (working)
				if(not ok and not comment.author == r.user.me() and comment.id not in replies):
					reply(comment)
					replies.append(comment.id)
					file = open('replies.txt', 'a')
					file.write(comment.id + '\n')
					file.close()
					ok = False
					break

def reply(parent):
	"""This function replies to comments
	Params: 
	parent - comment to reply to"""
	global num_replies
	print('new reply', file=sys.stderr)
	parent.reply("[mercy main btw](http://i.imgur.com/eYldgsG.jpg)")
	num_replies += 1

def delete(r):
	"""This function deletes all old comments
	Params: 
	r - reddit instance"""
	print('deleting comments', file=sys.stderr)
	acc = r.redditor(user)
	for comment in acc.comments.top(time_filter='all', limit=None):
		comment.delete()

def get_replies():
	"""This function retrieves all comments that have been replied to"""
	if not os.path.isfile('replies.txt'):
		return []
	file = open('replies.txt', 'r')
	replies = file.read()
	replies = replies.split('\n')
	file.close()
	return replies

main()