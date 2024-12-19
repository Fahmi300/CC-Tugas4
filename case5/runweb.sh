docker rm -f webapp
docker run -dit \
    --name webapp \
	-p 9999:3000 \
    -p 10000:5000 \
	mywebapp:1.0
