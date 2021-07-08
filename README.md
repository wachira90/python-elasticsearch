# python-elasticsearch
python-elasticsearch

## example

```
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

# allow up to 25 connections to each node
es = Elasticsearch(["172.16.1.10"], maxsize=25)

doc = {
    'fname': 'Wachira',
    'lname': 'Duangdee',
    'age': 36,
    'timestamp': datetime.now(),
}
res = es.index(index="user", id=1, body=doc)
print(res['result'])

res = es.get(index="user", id=1)
print(res['_source'])

es.indices.refresh(index="user")

res = es.search(index="user", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total']['value'])

for hit in res['hits']['hits']:
    print("%(timestamp)s %(fname)s: %(lname)s" % hit["_source"])
```

## for more info
```
https://elasticsearch-py.readthedocs.io/en/v7.13.3/
```
