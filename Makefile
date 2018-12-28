clean:
	rm -r output.txt

default:
	./ebpf_ic.py --hex --apart input.txt output.txt
	vim output.txt

test:
	python3 test.py
