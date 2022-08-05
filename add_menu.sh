# !/bin/bash
python manage.py migrate
fixtures=$(ls seed/)
while IFS= read -r fixture; do
    echo -n "Seeding "
    echo $fixture
    python manage.py loaddata seed/$fixture
done <<< "$fixtures"