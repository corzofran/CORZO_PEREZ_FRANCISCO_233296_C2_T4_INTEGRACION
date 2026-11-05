PY=python3
install: ; pip install -r requirements.txt && cd frontend && npm install
model: ; $(PY) -m spacy download es_core_news_lg
test: ; $(PY) -m pytest -q
test-frontend: ; ./run_with_server.sh bash -c 'cd frontend && BASE_URL=http://127.0.0.1:8000 npm test'
run: ; PYTHONPATH=. $(PY) -m uvicorn backend.app.main:app --port 8000
eval: ; PYTHONPATH=. $(PY) benchmark/eval_quality.py
loadtest: ; ./run_with_server.sh $(PY) benchmark/load_test.py --levels 1,10,25,50 --think-ms 500 --tag think500
loadtest-stress: ; ./run_with_server.sh $(PY) benchmark/load_test.py --levels 1,10,25,50 --think-ms 0 --tag stress
scalability: ; PYTHONPATH=. $(PY) benchmark/scalability.py
scrape: ; $(PY) scripts/scrape_corpus.py
corpus: ; $(PY) scripts/build_corpus.py && $(PY) scripts/build_qrels.py
report: ; $(PY) benchmark/make_report.py
