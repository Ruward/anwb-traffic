docker run --name anwb-listener \
    --network docker-network -d \
    -v /volume1/docker/anwb-traffic/programs.json:/listener/programs.json \
    -v /volume1/docker/anwb-traffic/.env:/listener/.env \
    --restart always \
    anwb-listener:latest