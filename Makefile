create_env:
	uv venv
	# 激活环境
	# source .venv/bin/activate

freeze:
	uv pip freeze > requirements.txt

sync:
	uv pip sync requirements.txt
