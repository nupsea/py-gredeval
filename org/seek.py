import redis
from redisgraph import Node, Edge, Graph


r = redis.Redis(host='localhost', port=6379)

redis_graph = Graph('cycle-data', r)

