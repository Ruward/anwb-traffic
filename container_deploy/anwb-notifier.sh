docker run --name anwb-notifier \
    --network docker-network \
    --network api-network \
    -v /volume1/docker/anwb-traffic/.env:/api/.env \
    -d anwb-notifier