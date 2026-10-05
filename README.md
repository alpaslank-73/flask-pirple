# Openshift v4.22

oc new-app quay.io/alpaslank/mysql-80:latest~https://github.com/alpaslank-73/container.git --name alp-mysql --context-dir=extend-image -e MYSQL_OPERATIONS_USER=opuser -e MYSQL_OPERATIONS_PASSWORD=oppass -e MYSQL_DATABASE=todo -e MYSQL_USER=alp -e MYSQL_PASSWORD=sifre123

oc new-app quay.io/alpaslank/python-39:latest~https://github.com/alpaslank-73/flask-pirple.git#openshift1 --name todo -e MYSQL_HOST=alp-mysql -e MYSQL_DATABASE=todo -e MYSQL_USER=alp -e  MYSQL_PASSWORD=sifre123 --context-dir=section3-todo-admin
