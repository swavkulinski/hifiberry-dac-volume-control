
place `vv_service` file in `/etc/init.d` folder

add execute permission for `vv_service` by executing `chmod 755 /etc/init.d/vv_service` 

place `volume` file in `/usr/local/bin` folder

add execute permission for `volume` by executing `chmod 755 /usr/local/bin/volume`

create pid file folder by executing `mkdir /var/run/vv_service` 

update rc by `update-rc.d vv_service defaults`

