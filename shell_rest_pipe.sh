#/bin/bash
curl -s https://jsonplaceholder.typicode.com/todos | jq -c '.[]' | xargs --null -n1 echo
