from flask import Flask
from redis import Redis
import json

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
@app.route('/<name>')
def hello(name):
    counts = json.loads(redis.get('hits')) or {'hits': 0, 'something-else': 'foo'}
    try:
         counts[name] += 1
    except KeyError:
         counts[name] = 1
    redis.set('hits', json.dumps(counts))
    return 'Hello {} I have been seen {} times.\n'.format(name,counts[name])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)