from sqlalchemy import create_engine
import pandas as pd

class Manager:
    __instance = None

    def __init__(self, engine=None, username=None, password=None, database=None, host=None, port=None):
        if Manager.__instance is None:
            self.engine_type = engine
            self.username = username
            self.password = password
            self.database = database
            self.host = host
            self.port = port
            self.url = self._generate_url()
            self.engine = create_engine(self.url)
            Manager.__instance = self
        else:
            raise Exception("Cannot create multiple instances of Database class")

    @staticmethod
    def get_instance(engine=None, username=None, password=None, database=None, host=None, port=None):
        if Manager.__instance is None:
            Manager(engine, username, password, database, host, port)
        return Manager.__instance

    def _generate_url(self):
        if self.engine_type == 'postgresql':
            return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.engine_type == 'mysql':
            return f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.engine_type == 'sqlite':
            return f"sqlite:///{self.database}"
        elif self.engine_type == 'oracle':
            return f"oracle://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.engine_type == 'mssql':
            return f"mssql+pymssql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        else:
            raise Exception("Unsupported engine type")

    def execute_query(self, query):
        with self.engine.connect() as conn:
            result = conn.execute(query)
            data = pd.DataFrame(result.fetchall(), columns=result.keys())
        return data