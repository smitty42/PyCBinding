
Setup WSL:
https://learn.microsoft.com/en-us/windows/wsl/install

To run GCC on Windows:
https://jamesmccaffrey.wordpress.com/2017/02/10/compiling-and-running-a-c-program-in-bash-on-windows-10/


You may need to make sure that the project files are owned by your WSL Linus users: `sudo chown my_user *`
Further, you may need to configure WSL for `chown` to work:
https://stackoverflow.com/questions/46610256/chmod-wsl-bash-doesnt-work

To create the shared object Python will link to:

`gcc -fPIC -shared -o pi.so pi.c` 

To test your C without Python:

`gcc -o pi pi.c -lm`


Setup the python env with `uv sync; /venv/bin/activate`

Run the script with `python pi.py`
This should compute Pi with a Taylor series simultaneously in Python directly
and in C. You can observe that the C implementation being called from Python
converges to the true value of Pi faster than the pure Python implementation.
