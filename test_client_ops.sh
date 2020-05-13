while [[ 1 ]]; do
    curl -X POST -H 'Content-Type: application/json' -H 'fid_timestamp_unix_ns: 10' -d '{"lines": ["12345"]}' http://localhost:9999/project/5620bece05509b0a7a3cbc61/doc/111122223320

    sleep 0.01

    curl -v http://localhost:9999/project/5620bece05509b0a7a3cbc61/doc/111122223320

    sleep 0.01
done