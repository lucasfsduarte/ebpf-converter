# How to run Load Balancer

* Download the repository with libraries:
```
git clone --recurse-submodules https://github.com/Netronome/bpf-samples.git
```

* Download and install Linux Kernel v4.17.x:
```
wget -c kernel.ubuntu.com/~kernel-ppa/mainline/v4.17.1/linux-headers-4.17.1-041701_4.17.1-041701.201806111730_all.deb

sudo dpkg -i linux-headers-4.17.1*.deb linux-image-4.17.1*.deb
```
Wait the dpkg to finish the process and then restart the system.

* Install clang and llvm:
```
sudo apt-get install clang
sudo apt-get install llvm
```

* Replace bpf.h in /usr/include/linux with the file in /usr/src/linux-headers-4.17.x/include/uapi/linux. You can do that by creating a symbolic link or through a direct copy.

* Download the folder `lbgen` and copy it's content to `bpf-samples/l4lb/`. Then, run:

```
chmod +x gen.sh

make

./gen.sh l4lb_xdp
```
* eBPF instructions will be at instructions.txt and l4lb_xdp.dis as hexadecimal netfpga pattern and ebpf assembly format, respectively.

------------------------------------------------------------------------------------------------------------
### References

1. https://itsfoss.com/upgrade-linux-kernel-ubuntu/

2. https://superuser.com/questions/1280068/how-do-i-install-clang-4-0-on-ubuntu-14-04

3. https://github.com/vmware/p4c-xdp/issues/56
