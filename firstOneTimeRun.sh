sudo apt-get install flameshot -y
sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config -y
pip install pytesseract pyperclip
sudo cp image2text.py /
sudo cp image2textSR /usr/local/bin/
sudo chmod +x /usr/local/bin/image2textSR
