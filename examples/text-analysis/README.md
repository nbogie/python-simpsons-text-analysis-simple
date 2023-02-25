# simpsons-text-analysis

Very simple example first non-trivial python project

-   Downloads simpsons episodes (JSON) using `requests` library.
-   Studies their summaries using `textblob` library,
    -   strips html tags out using `re` library
-   builds an index of the noun-phrases in each, against the episodes they occur in.

### installation

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m textblob.download_corpora --lite
```

### run

```
python main.py
```

### Example output:

```
aerosmith [(3, 10), (22, 22)]
ralph wiggum [(9, 18), (19, 10)]
nuclear plant [(26, 12), (26, 14), (28, 5)]
groundskeeper willie [(7, 6), (12, 8), (19, 13), (21, 6), (26, 22)]
...
```
