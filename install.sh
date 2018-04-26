#!/bin/bash

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
pip3 install pip Pinyin request pq pyperclip xpinyin pyquery
cp DiaryPin.py ~/DiaryPin.py
echo "alias today='python3 ~/DiaryPin.py'" >> ~/.bashsrc
chmod 777 ~/.bashsrc
echo "source ~/.bashsrc" >> ~/.bash_profile