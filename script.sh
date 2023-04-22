#! /bin/bash

clear
sleep 2
echo "Install Dependences & Webdriver..."
sleep 1
sudo apt update | tee -a ./apt_update.log
echo "....."
echo "Update done, check apt_update.log for details."
sleep 2
clear
sudo apt install -y \
chromium-browser=112.0.5615.49-0ubuntu0.18.04.1 \
chromium-chromedriver=112.0.5615.49-0ubuntu0.18.04.1 \
| tee -a ./apt_install.log
echo "....."
echo "Install done, check apt_install.log for details."
sleep 2
clear
echo "Prepare Keepalive Script..."
sleep 1
pip3 install -q selenium==3.141.0 | tee -a ./pip_install.log
echo "....."
echo "Pip done, check pip_install.log for details."
sleep 2
clear
wget -q -O main.py https://github.com/MtflML/FirstProject/raw/main/main.py
echo "Begin To Execute Python3 Script..."
nohup python3 ./main.py &
echo "Start KeepOnline Workflow!Enjoy it!"
sleep 3
clear
