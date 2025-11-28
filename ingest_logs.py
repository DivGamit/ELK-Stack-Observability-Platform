import re
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

pattern = r"(.*?)\s+(INFO|WARN|ERROR)\s+(.*)"

with open("app.log") as f:
    for line in f:
        m = re.match(pattern, line.strip())
        if m:
            doc = {
                "timestamp": m.group(1),
                "level": m.group(2),
                "service": m.group(3).split()[0],
                "message": " ".join(m.group(3).split()[1:])
            }
            es.index(index="fake_logs", document=doc)

print("Logs sent to Elasticsearch.")
