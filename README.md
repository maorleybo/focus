# focus
focus

# build environment
built in manjaro linux with pipenv for easy libraries installation

## install
I use pipenv so you need to clone the repo and install using: ```pipenv install```.

to enter the venv, use: ```pipenv shell```

* if you want to open in visual studio code:
    * you need to set the python interpreter to the venv so:
        *     
            1. CTRL - SHFT - P
            2. Python: Set interpreter
            3. get your venv dir using ```pipenv --venv```
            4. add the interpreter in *(<venv_DIR>/bin/python)*

        * 
            1. get you direct interpreter location using ```pipenv --py```
            2. CTRL - SHFT - P
            3. Python: Set interpreter
            4. add the interpreter in *(<venv_DIR>/bin/python)*
    either way works