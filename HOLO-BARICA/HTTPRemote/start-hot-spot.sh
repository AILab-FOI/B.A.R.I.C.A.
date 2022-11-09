# OVO JEDINO RADI: https://github.com/oblique/create_ap

# https://askubuntu.com/questions/180733/how-to-setup-an-access-point-mode-wi-fi-hotspot/180734#180734
# prije toga je bilo ovo, pa ako nešto fali, moguće je da je tu:
# http://askubuntu.com/questions/323335/how-to-set-up-a-wi-fi-hotspot-with-an-ubuntu-laptop-access-point-mode
# ili ovo:
# http://askubuntu.com/questions/180733/how-to-setup-an-access-point-mode-wi-fi-hotspot

# Za vraćanje na staro:
# For normal wifi comment out 

#auto wlan0
#iface wlan0 inet static
#address 10.10.0.1
#netmask 255.255.255.0

# in /etc/network/interfaces

# ovo je vjerojatno nepotrebno
#sudo service isc-dhcp-server restart
#sudo service hostapd restart


sudo create_ap -n wlan0 --no-virt brain4games braindrain &

echo "If it doesn't work: read the scriptfile, dumbass ;-)"
