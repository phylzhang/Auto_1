import os
import configparser
try:##python3中
    import configparser
except:###python2中
    import ConfigParser as configparser
cur_path=os.path.dirname(os.path.realpath(__file__))
configpath=os.path.join(cur_path,"cfg.ini")
conf= configparser.ConfigParser()
conf.read(configpath,encoding='UTF-8')

smtp_server=conf.get("email","smtp_server")
sender=conf.get("email","sender")
psw=conf.get("email","psw")
receiver=conf.get("email","receiver")
port=conf.get("email","port")
