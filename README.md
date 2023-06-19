# machine_learning_project

'conda --version'
' conda create -p venv python==3.7'
'conda activate venv/'

'pip install -r requirements.txt'

to addd filr to git
'git add <file name>'

To create version/commit all chnages by git
'git commit -m "message"'

To send version  to git hub
'git push origin main'

To chek remote url
'git remote -v'

#To setup CI/CD piplene in heroku we need 3 information

1.HEROKU_EMAIL='harshal10200@gmail.com'
2.HEROKU_API_KEY='8e7c56ff-8894-41a8-8cd6-87a3d8ca664c'
3.HEROKU_API_NAME=

BUILD DOCKER IMGE

'docker build -t <image_name>:<tagname>.'
note =imagname for docker must be in lower case

To list docker img
'docker images'

RUN docker images
'docker run -p 5000:5000 -e PORT=5000 <IMGID>'

TO cheak running container in docker
'docker ps'

To stop the container
'docker stop<container_id>'

