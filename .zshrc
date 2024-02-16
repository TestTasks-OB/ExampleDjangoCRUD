alias find80='lsof -nP -i4TCP:80  | grep LISTEN' #look for open ports 80
alias dcbuild='docker-compose up --build' 
alias dcdown='docker-compose down'
alias runserver='python manage.py runserver'