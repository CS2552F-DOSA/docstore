while [[ 1 ]]; do
    curl -X POST -H 'Content-Type: application/json' -d '{"lines": ["123"]}' http://localhost:9999/project/5620bece05509b0a7a3cbc61/doc/111122223320

    sleep 1

    curl -v http://localhost:9999/project/5620bece05509b0a7a3cbc61/doc/111122223320

    sleep 1
done