sudo docker build -t notifications-api .
sudo docker run -d -p 8081:8080 --name notifications-api notifications-api