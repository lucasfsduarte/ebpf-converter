# How to run Load Balancer

Download the repository with libraries:
```
git clone --recurse-submodules https://github.com/Netronome/bpf-samples.git
```

Download and install Linux Kernel v4.17.x:
```
wget -c kernel.ubuntu.com/~kernel-ppa/mainline/v4.17.1/linux-headers-4.17.1-041701_4.17.1-041701.201806111730_all.deb

sudo dpkg -i linux-headers-4.17.1*.deb linux-image-4.17.1*.deb
```
Wait the dpkg to finish the process and then restart the system.

3. Install clang and llvm:
	sudo apt-get install clang
	sudo apt-get install llvm

	If errors appears, use sudo apt-get -f install then repeat the last command above.

4. Replace bpf.h in /usr/include/linux with the file in /usr/src/linux-headers-4.17.x/include/uapi/linux
   by creating a symbolic link or direct copy.

5. Run make inside to obtain the .o file.

6. Run ./gen to obtain the instructions.txt file.

------------------------------------------------------------------------------------------------------------
References:

2. https://itsfoss.com/upgrade-linux-kernel-ubuntu/

3. https://superuser.com/questions/1280068/how-do-i-install-clang-4-0-on-ubuntu-14-04

4. https://github.com/vmware/p4c-xdp/issues/56
