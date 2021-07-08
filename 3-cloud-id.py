from elasticsearch import Elasticsearch

es = Elasticsearch(
    cloud_id="cluster-1:dXMa5Fx...",
    http_auth=("elastic", "<password>"),
)
