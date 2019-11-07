test:
	coverage run test_rpn.py
	coverage report
	coverage-badge -o coverage.svg -f
.PHONY: test
