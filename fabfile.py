from fabric.api import local

def tests():
    commands = [
        "export PYTHONPATH=.",
        "export ASYNC_TEST_TIMEOUT=60",
        "coverage run --source=. -m unittest discover -s tests/",
        "coverage report -m",
    ]
    local(' ; '.join(commands))
