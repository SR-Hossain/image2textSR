s = open('firstOneTimeRun.sh').read()
s = s.replace('apt-get', 'pamac')
with open('firstOneTimeRun.sh', 'w') as f:
	f.write(s)
