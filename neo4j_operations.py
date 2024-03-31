import os
from neo4j import GraphDatabase


class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(
                self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def create_sentence(self, text):
        with self.__driver.session() as session:
            cypher_query = "CREATE (n:Sentence {id:randomUUID(), text:$text})"
            session.run(cypher_query, text=text)


# Aura DB credentials
uri = os.environ.get('NEO4J_URI')
user = os.environ.get('NEO4J_USER')
password = os.environ.get('NEO4J_PASSWORD')

# Create a global Neo4j connection instance
neo4j_conn = Neo4jConnection(uri, user, password)
