
run-local:
	uvicorn --factory main:create_app --host 0.0.0.0 --port 8000 --reload


docker-build:
	sudo docker-compose up --build -d

docker-down:
	sudo docker-compose down

logs:
	sudo docker logs -f test_app


create-branch:
	git checkout -b $(BRANCH)
