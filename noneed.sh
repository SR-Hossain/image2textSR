sudo apt install flameshot -y
sudo apt install python3-pip
sudo apt install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config -y
pip3 install pytesseract pyperclip
sudo cp image2text.py /
sudo cp image2textSR /usr/local/bin/
sudo chmod +x /usr/local/bin/image2textSR
