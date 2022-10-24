# ABOUT
simple example of web server to reply with ping results to selective URI

## videos 
in Ukrainian: 

[![how-to video (in Ukrainian)](https://img.youtube.com/vi/GBfXyyZU-C4/0.jpg)](https://www.youtube.com/watch?v=GBfXyyZU-C4)


# HOWTO 
## INSTALL
```
mkdir /opt/echopingws
cp echopingws.py /opt/echopingws
cp settings.json /opt/echopingws

sudo cp echopingws.service /etc/systemd/system

sudo systemctl daemon-reload 
```
## Start
```sudo service echopingws restart```

## CHECK STATUS
```sudo service echopingws status```

to check logs
``` journalctl -u echopingws```

## CHANGE SETTINGS
modify /opt/echopingws/settings.json and restart
