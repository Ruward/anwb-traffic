docker run --name anwb-notifier \
    --network docker-network \
    -v /volume1/docker/anwb-traffic/.env:/api/.env \
    -d anwb-notifier

docker network connect api-network anwb-notifier