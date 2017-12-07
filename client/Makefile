DL=`ldd /bin/ls | grep "libdl.so" | awk '{ print $$3 }'`
LIBC=`ldd /bin/ls | grep "libc.so" | awk '{ print $$3 }'`
DEBUG=1

all: preload.c
	echo "#define LIBC \"${LIBC}\"" > preload.h
	gcc -rdynamic -shared -fPIC -o preload.so preload.c ${DL}

debug: preload.c
	echo "#define LIBC \"${LIBC}\"" > preload.h
	echo "#define DEBUG" >> preload.h
	gcc -rdynamic -shared -fPIC -o preload.so preload.c ${DL}
