#!/bin/sh

# Run this file to remove the example code from the project.
# ; ./remove_example_code.sh

echo "This will remove the example code from the project."
echo "DO NOT RUN THIS IF YOU HAVE ADDED YOUR OWN CODE."
echo "It may accidentally delete your code!"
echo "Continue? [y/N]"
read -r response
if [ "$response" != "y" ]; then
    echo "Aborting."
    exit 1
fi

rm lib/album_repository.py
rm lib/album.py
rm tests/test_album_repository.py
rm tests/test_album.py
rm tests/test_example_routes.py
rm example_routes.py
rm seeds/album_store.sql

grep -v album_store seed_dev_database.py > seed_dev_database.py.tmp
mv seed_dev_database.py.tmp seed_dev_database.py

sed -n -e '/== Example Code Below ==/{' -e ':a' -e 'N' -e '/== End Example Code ==\n/!ba' -e 's/.*//' -e '}' -e 'p' app.py > app.py.tmp
mv app.py.tmp app.py

sed -n -e '/== Example Code Below ==/{' -e ':a' -e 'N' -e '/== End Example Code ==\n/!ba' -e 's/.*//' -e '}' -e 'p' tests/test_app.py > tests/test_app.py.tmp
mv tests/test_app.py.tmp tests/test_app.py

rm remove_example_code.sh

echo "Completed."
