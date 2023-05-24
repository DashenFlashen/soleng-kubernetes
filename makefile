install:
	test -d venv || python3 -m venv ./venv
	. venv/bin/activate; pip install --upgrade pip; pip install -Ur scripts/requirements.txt

clean:
	rm -rf venv
