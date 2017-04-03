echo "OS Version"
lsb_release -a

echo "Architecture"
uname -i

echo "Memory Usage"
free -m | grep -B1 "Mem:"

echo "IP config"
ifconfig

