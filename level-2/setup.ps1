virtualenv -p python2 google-foobar-lvl-2
./google-foobar/google-foobar-lvl-2/Scripts/Activate.ps1
./google-foobar/google-foobar-lvl-2/Scripts/python.exe -m pip install --upgrade pip
python2 -m pip install -r requirements.txt
pip freeze > requirements.txt