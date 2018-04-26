#!/bin/bash

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
pip3 install Pinyin
pip3 install request
pip3 install pq
pip3 install pyperclip
pip3 install xpinyin
pip3 install pyquery
cp DiaryPin.py ~/DiaryPin.py
echo "alias today='python3 ~/DiaryPin.py'" >> ~/.bashsrc
chmod 777 ~/.bashsrc
echo "source ~/.bashsrc" >> ~/.bash_profile