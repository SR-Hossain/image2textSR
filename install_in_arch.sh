sudo pacman install tesseract-data-eng --noconfirm
pip install pytesseract pyperclip --break-system-packages
python3 arch.py
sudo cp image2text.py /
sudo cp image2textSR /usr/local/bin/
sudo chmod +x /usr/local/bin/image2textSR
