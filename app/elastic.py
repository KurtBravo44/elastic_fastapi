from elasticsearch import AsyncElasticsearch

es = AsyncElasticsearch("http://elasticsearch:9200")


async def search_documents(query: str):
    response = await es.search(
        index="documents",
        body={
            "query": {
                "match": {
                    "text": query
                }
            },
            "size": 20,
            "sort": [
                {"created_date": {"order": "desc"}}
            ]
        }
    )
    return response['hits']['hits']
