#!/bin/sh
# Inline version:
# find . -wholename "./*/migrations" -prune -o -wholename "./docs/*" -prune -o -name "*\.py" -exec pep8 {} \;

final_exit=0
for file in $(find . -wholename "./*/migrations" -prune -o -wholename "./docs/*" -prune -o -name "*\.py" -print); do
    pep8 "$file"
    if [ $? -ne 0 ]; then
        final_exit=1
    fi
done

if [ $final_exit -ne 0 ]; then
    echo "PEP8 compliance test failed, aborting commit."
    exit
fi

pid=$(ps aux | grep "./manage.py runserver" | grep -v grep | head -1 | xargs | cut -f2 -d" ")

if [[ -n "$pid" ]]; then
    kill $pid
fi

./manage.py runserver
