# Загрузка DICOM файлов из архива в orthanc

команды для сборки контейнера
docker build mongo_metadata -t mongo_metadata
docker run --network host --name mongo_metadata -it mongo_metadata
docker run --network host -v storage:/data --name mongo_metadata -it mongo_metadata
