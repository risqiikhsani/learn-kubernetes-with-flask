docker build -t simple-flask:latest .
docker run --name simple-flask -d -p 5000:5000 -e DATABASE_URL="localhost" simple-flask
docker stop simple-flask

docker tag simple-flask:latest risqiikhsani/simple-flask:latest
docker login (if not logged in)
docker push risqiikhsani/simple-flask:latest