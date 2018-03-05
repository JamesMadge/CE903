# J.Madge 01.03.2018 Update existing packages.
echo ----------------------------------------
echo Updating existing packages.
echo ----------------------------------------

sudo apt-get update
sudo apt-get upgrade

# J.Madge 01.03.2018 Install Git.
# J.Madge 01.03.2018 https://gist.github.com/derhuerst/1b15ff4652a867391f03
echo ----------------------------------------
echo Intall Git.
echo ----------------------------------------
sudo apt-get install git

# J.Madge 01.03.2018 Install `Python 3.6' & `pip3'.
# J.Madge 01.03.2018 http://docs.python-guide.org/en/latest/starting/install3/linux/
# J.Madge 01.03.2018 https://docs.bigchaindb.com/projects/server/en/latest/appendices/install-latest-pip.html
echo ----------------------------------------
echo Installing Python 3.6 and pip3.
echo ----------------------------------------
sudo apt-get install python3.6
sudo apt-get install python3-pip

# J.Madge 01.03.2018 Install `numpy'.
# J.Madge 01.03.2018 https://www.scipy.org/install.html
echo ----------------------------------------
echo Installing numpy.
echo ----------------------------------------
pip3 install numpy

# J.Madge 01.03.2018 Install `xautomation'.
# J.Madge 01.03.2018 https://www.howtoinstall.co/en/ubuntu/trusty/xautomation
echo ----------------------------------------
echo Installing xautomation.
echo ----------------------------------------
sudo apt-get install xautomation

# J.Madge 01.03.2018 Install `OpenAI-Gym' with full set of environments.
# J.Madge 01.03.2018 https://github.com/openai/gym
echo ----------------------------------------
echo Installing OpenAI-Gym with full set of environments.
echo ----------------------------------------
pip3 install gym
sudo apt-get install -y python-numpy python-dev cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig

# J.Madge 01.03.2018 Clone 'gym_torcs' repository.
echo ----------------------------------------
echo Cloning gym-torcs repository.
echo ----------------------------------------
git clone https://github.com/ugo-nama-kun/gym_torcs.git
# TODO Change content of the errornous file: `gym_torcs/vtorcs-RL-color/src/drivers/olethros/geometry.cpp', line 373 replace `isnan' with `std::isnan'.

# J.Madge 01.03.2018 Changed 'libpng12-dev' to 'libpng-dev', the former is no longer available.
echo ----------------------------------------
echo Installing packages required for vtorcs-RL-color
echo ----------------------------------------
sudo apt-get install libglib2.0-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev  libplib-dev libopenal-dev libalut-dev libxi-dev libxmu-dev libxrender-dev libxrandr-dev libpng-dev

echo ----------------------------------------
echo Installing vtorcs-RL-color
echo ----------------------------------------
cd gym_torcs/vtorcs-RL-color/
./configure
sudo make
sudo make install
sudo make datainstall

# TODO Move the bin file from where it has been installed to where it is expected.

















# # J.Madge 01.03.2018 TODO These are thing I tried when installing torcs, I'm not sure if they were important or not. Leave them here just in case!

# https://github.com/ugo-nama-kun/gym_torcs/tree/master/vtorcs-RL-color
# J.Madge 01.03.2018 Download dependancies.
# J.Madge 01.03.2018 Changed 'libpng12-dev' to 'libpng-dev', the former is no longer available.
#sudo apt-get install libglib2.0-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev libplib-dev libopenal-dev libalut-dev libxi-dev libxmu-dev libxrender-dev libxrandr-dev libpng-dev

# http://cicolink.blogspot.co.uk/2012/10/how-to-compile-and-install-torcs-on.html
# J.Madge 01.03.2018 Removed duplicate packaged from the command above.
# J.Madge 01.03.2018 Changed `libxine-dev' to `libxine2-dev' as it is no longer available.
#sudo apt-get install build-essential libxmu6 libxi-dev libxine2-dev libalut-dev freeglut3 cmake libogg-dev libvorbis-dev libxxf86dga-dev libxxf86vm-dev zlib1g-dev

# J.Madge 01.03.2018 Could solve the issue of not being able display windows as root?
# https://askubuntu.com/questions/614387/gksu-gtk-warning-cannot-open-display-0
# xhost +SI:localuser:root

# `plib 1.8.5' https://launchpad.net/ubuntu/+source/plib/1.8.5-7
# Download from the above site.
# tar xvzf plib_1.8.5.orig.tar.gz
#cd plib-1.8.5
#./configure CFLAGS="-O2 -m64 -fPIC" CPPFLAGS="-O2 -fPIC" CXXFLAGS="-O2 -fPIC" LDFLAGS="-L/usr/lib64"
#sudo make install
#cd ..

# `openal-soft' https://github.com/kcat/openal-soft
# git clone https://github.com/kcat/openal-soft
#cd openal-soft
#cd cmake
#cmake ..
#sudo make
#sudo make install
#cd ../..

# `Freealut' https://directory.fsf.org/wiki/Freealut
# tar xvzf freealut_1.1.0.orig.tar.gz
#cd freealut-1.1.0
#./configure
#sudo make
#sudo make install
#cd ..

# J.Madge 01.03.2018 Clone 'gym_torcs' repository.
#git clone https://github.com/ugo-nama-kun/gym_torcs.git

# J.Madge 01.03.2018 Change into the 'vtorcs-RL-color/' directory.
#cd gym_torcs/vtorcs-RL-color/
#./configure CFLAGS="-O2 -m64 -fPIC" CPPFLAGS="-O2 -fPIC" CXXFLAGS="-O2 -fPIC" LDFLAGS="-L/usr/lib64"
#sudo make
#sudo make install
#sudo make datainstall
