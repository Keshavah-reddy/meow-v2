<h1 align="center">meow-v2</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>


### [√] Description :

***Ultimate phishing tool in python. Includes popular websites like facebook, twitter, instagram, github, reddit, gmail and many others.***

### [*]Announcent

This project is now a part of [Meow](https://github.com/keshavah-reddy/Meow). Further bug fixes and feature addition will be available in that


### [+] Installation

##### Install dependencies (git, python, php ssh)

 - For Debian (Ubuntu, Kali-Linux, Parrot)
    - ```sudo apt install git python3 php openssh-client -y```
 - For Arch (Manjaro)
    - ```sudo pacman -S git python3 php openssh --noconfirm```
 - For Redhat(Fedora)
    - ```sudo dnf install git python3 php openssh -y```
 - For Termux
    - ```pkg install git python3 php openssh -y```

##### Clone this repository

 - ```git clone https://github.com/keshavah-reddy/meow-v2```

##### Enter the directory
 - ```cd meow-v2```

##### Install all modules
 - ```pip3 install -r files/requirements.txt```

##### Run the tool
 - ```python3 meow-v2.py```

#### Or, directly run
```
wget https://raw.githubusercontent.com/keshavah-reddy/meow-v2/main/meow-v2.py && python3 meow-v2.py

```

### Pip
 - `pip3 install meow-v2` [For Termux]
 - `sudo pip3 install meow-v2` [For Linux]
 - `meow-v2`

### Docker

 - `sudo docker pull keshavah-reddy/meow-v2`
 - `sudo docker run --rm -it keshavah-reddy/meow-v2`

### Support

OS         | Support Level
-----------|--------------
Linux      | Excellent
Android    | Excellent
iPhone     | Alpha (Recommended docker)
MacOS      | Alpha (Recommended docker)
Windows    | Unsupported (Use docker/virtual-box/vmware)
BSD        | Never tested

#### Options

```
usage: meow-v2.py [-h] [-p PORT] [-o OPTION] [-t TUNNELER]
                    [-r REGION] [-s SUBDOMAIN] [-u URL] [-m MODE]
                    [-e TROUBLESHOOT] [--nokey] [--noupdate]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  meow-v2's server port [Default : 8080]
  -o OPTION, --option OPTION
                        meow-v2's template index [Default : null]
  -t TUNNELER, --tunneler TUNNELER
                        Tunneler to be chosen while url shortening
                        [Default : Cloudflared]
  -r REGION, --region REGION
                        Region for loclx [Default: auto]
  -s SUBDOMAIN, --subdomain SUBDOMAIN
                        Subdomain for loclx [Pro Account]
                        (Default: null)
  -u URL, --url URL     Redirection url after data capture [Default :
                        null]
  -m MODE, --mode MODE  Mode of meow-v2 [Default: normal]
  -e TROUBLESHOOT, --troubleshoot TROUBLESHOOT
                        Troubleshoot a tunneler [Default: null]
  --nokey               Use localtunnel without ssh key [Default:
                        False]
  --noupdate            Skip update checking [Default : False]
```

### Features:

 - Multi platform (Supports most linux)
 - Easy to use
 - Possible error diagnoser
 - 77 Website templates
 - Concurrent 3 tunneling (Cloudflared, Loclx and LocalHostRun)
 - Upto 6 links for phishing
 - OTP Support
 - Argument support
 - Credentials mailing
 - Built-in masking of URL
 - Custom masking of URL
 - URL Shadowing
 - Redirection URL settings
 - Portable file (Can be run from any directory)
 - Get IP Address and many other details along with login credentials


### Requirements

 - `Python(3)`
   - `requests`
   - `bs4`
   - `rich`
 - `PHP`
 - `SSH`
 - 900MB storage
 
If not found, php and python modoules will be installed on first run

#### Tested on

 - `Termux`
 - `Ubuntu`
 - `Kali-Linux`
 - `Arch`
 - `Fedora`
 - `Manjaro`

## Usage

1. Run the script
2. Choose a Website
3. Wait sometimes for setting up all
4. Send the generated link to victim
5. Wait for victim login. As soon as he/she logs in, credentials will be captured

<h1 align="center">Example</h1>

![meow-v2](https://raw.githubusercontent.com/Keshavah-reddy/meow-v2/main/files/meow-v2.gif)


**Users can decide where the victim will be redirected after data is captured**

## Solution of common issues
 - Some secured browsers like Firefox can warn for '@' prefixed links. You should use pure links or custom link to avoid it.
 - Termux from play store in not supported. Download termux from fdroid or github
 - VPN or proxy prevents tunneling and even proper internet access. Turn them off you have issues.
 - Some android requires hotspot to start Cloudflared and Loclx. If you face 'tunneling failed' in android, most probably your hotspot is turned off. Turn it on and keep it on untill you close Meow-v2.
 - If you want mailing credentials then you need to use app password. Visit [here](https://myaccount.google.com/u/0/apppasswords) and generate an app password, put that in `files/email.json`. You may need to enable 2FA before it.
 
## [!] Disclaimer
***This tool is developed for educational purposes. Here it demonstrates how phishing works. If anybody wants to gain unauthorized access to someones social media, he/she may try out this at his/her own risk. You have your own responsibilities and you are liable to any damage or violation of laws by this tool. The author is not responsible for any misuse of Meow-v2.0***

### This repository is open source to help others. So if you wish to copy, consider giving credit!



### [*] Support
####  Want to show support? Just spread the word and smash the star button
###### Donate UPI: ***keshava6677@ybl (or) @ibl (or) @axl ***

## [~] Find Me on :

- [![Github](GITHUB)](https://github.com/Keshavah-reddy)


- [![Telegram](TELEGRAM)](https://t.me/keshav_vah)

