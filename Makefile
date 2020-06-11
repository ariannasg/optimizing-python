.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: security
security:
	safety check