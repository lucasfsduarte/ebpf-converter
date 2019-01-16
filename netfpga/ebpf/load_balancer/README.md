1. Download the repository with libraries:
	git clone --recurse-submodules https://github.com/Netronome/bpf-samples.git

2. Update Linux Kernel to 4.17.x

	uname -sr (follow the next steps only if the current kernel is lower than 4.17)
	sudo add-apt-repository ppa:teejee2008/ppa
	sudo apt-get update
	sudo apt-get install ukuu
	ukuu
	
	Wait the program to finish load data, select 4.17 version and click in install.
	Wait the program to finish the process and then restart the system.

3. Install clang-4.0 and llvm-4.0:
	sudo apt-add-repository "deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty-4.0 main"
	sudo apt-get update
	sudo apt-get install clang-4.0 lldb-4.0
	
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

	
	
