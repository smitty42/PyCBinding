
Setup WSL:
https://learn.microsoft.com/en-us/windows/wsl/install

To run GCC on windows:
https://jamesmccaffrey.wordpress.com/2017/02/10/compiling-and-running-a-c-program-in-bash-on-windows-10/


You may need to make sure that the project files are owned by your wsl linus users: `sudo chown my_user *`
And you may need to configure wsl for `chown` to work:
https://stackoverflow.com/questions/46610256/chmod-wsl-bash-doesnt-work

To create the shared object python will link to:

`gcc -fPIC -shared -o pi.so pi.c` 

To test your C without python:

`gcc -o pi pi.c -lm`


Setup the python env with `uv sync; /venv/bin/activate`

Run the script with `python pi.py`
This should compute Pi with a Talor series simultaneously in python directly
and in C. You can observe the the C implementation being called from python
converges to the true value of Pi faster then the pure python implementation.
