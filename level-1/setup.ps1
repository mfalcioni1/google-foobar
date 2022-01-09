virtualenv -p python2 google-foobar-lvl-1
./google-foobar/google-foobar-lvl-1/Scripts/Activate.ps1
./google-foobar/google-foobar-lvl-1/Scripts/python.exe -m pip install --upgrade pip
python2 -m pip install -r requirements.txt
pip freeze > requirements.txt