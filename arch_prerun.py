s = open('firstOneTimeRun.sh').read()
s = s.replace('apt-get', 'pamac')
s = s.replace('sudo apt-get install flameshot -y', 'sudo pacman -S flameshot --noconfirm')
s = s.replace('sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config -y', 'sudo pacman -S tesseract-data-eng --noconfirm')
with open('firstOneTimeRun.sh', 'w') as f:
	f.write(s)
