sudo add-apt-repository ppa:webupd8team/java -y
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java8-set-default


#install anoconda

wget https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh
sudo apt install python-pip

python -m spacy.en.download all
sudo apt-get install g++
pip install probablepeople

# check info
storage: df -h
memory: free -m -h
cpu: cat /proc/cpuinfo
