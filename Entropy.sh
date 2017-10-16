#Crypt - Entropy
#Resource: https://random-notes-of-a-sysadmin.blogspot.com/2016/04/is-raspberry-pi-suitable-and-safe-to.html?m=1

#Assumption
#Since /dev/urandom is a Hash chain seeded from /dev/random, then you could actually predict the next numbers, if you knew the seed. If you have enough control over the entropy pool, then from the output of /dev/urandom you might be able to guess this seed, which would enable you to predict all the next numbers from /dev/urandom, but only if you keep /dev/random exhausted, otherwise /dev/urandom will be reseeded.

####################################
#Setup
sudo apt-get update
sudo apt-get install -y netpbm
sudo apt-get install -y pv
sudo apt-get install -y rng-tools
#Check for hardware entropy service
#ps -e | grep rn #Look for rngd
#We just needs the tools not the service itself
sudo /etc/init.d/rng-tools stop
sudo update-rc.d rng-tools remove
sudo date -s '@99999' 
sudo reboot
####################################

####################################
#Run Entropy Monitors
#Check the amount of entropy in the pool 
while sleep 3; do cat /proc/sys/kernel/random/entropy_avail; done
#Start FIPS Test. Note .01% of failures is normal
sudo cat /dev/urandom | rngtest -t 2
####################################

####################################
#Try to empty the entropy pool using /dev/random. Do this in multiple instances of "screen"
sudo nice -n -20 dd if=/dev/random | pv | dd of=/dev/null
####################################

####################################
#Reduce Entropy Source by setting the date to a time close to epoch
sudo systemctl disable systemd-timesyncd.service
date
#date -d ‘@2270’
sudo date -s '@99999' 
date
####################################

####################################
#Reduce Entropy by seeding low entropy data into the entropy pool using urandom itself.
#This should work if the pool remains low and /dev/random remains exhausted
#rngd --foreground --rng-device=/dev/zero --rng-quality=low --random-step=2500
sudo rngd --foreground --rng-device=/dev/urandom --rng-quality=low --random-step=2500
####################################

####################################
#Do FIPs test 
sudo cat /dev/urandom | rngtest -c 1000
####################################

