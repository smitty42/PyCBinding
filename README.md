gcc -fPIC -shared -o pi.so pi.c 
gcc -o pi pi.c -lm
