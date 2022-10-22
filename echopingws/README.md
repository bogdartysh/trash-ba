# ABOUT
simple example of web server to reply with ping results to selective URI
# HOWTO 
## INSTALL
```
mkdir /opt/echopingws
cp echopingws.py /opt/echopingws
cp settings.json /opt/echopingws

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
