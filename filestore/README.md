команды для сборки контейнера
docker build filestore -t filestore
docker run --network host --name filestore -it filestore
docker run --network host -v storage:/data --name filestore -it filestore
