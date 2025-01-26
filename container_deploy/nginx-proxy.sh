docker run --name nginx-proxy \
    --network bridge \
    -p 100:100 \
    -v /volume1/docker/ntfy/cert:/etc/cert \
    -v /volume1/docker/nginx/default.conf:/etc/nginx/conf.d/default.conf \
    -d nginx 