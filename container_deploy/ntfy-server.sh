docker run --name ntfy-server \
    --network docker-network \
    -v /volume1/docker/ntfy/config:/etc/ntfy \
    -v /volume1/docker/ntfy/webpush/webpush.db:/var/cache/ntfy/webpush.db \
    -v /volume1/docker/ntfy/cert:/etc/cert \
    -v /volume1/docker/ntfy/access:/var/lib/ntfy \
    -d ntfy serve