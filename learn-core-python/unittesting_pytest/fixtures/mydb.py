class MyDB:
    def __init__(self):
        self.connection = Connection()

    def connect(self, connection_string):
        return self.connection


class Connection:
    def __init__(self):
        self.cur = Cursor()

    def cursor(self):
        return self.cur

    def close(self):
        pass


class Cursor:
    def __init__(self):
        self._result = None

    def execute(self, query):
        if query == "select id from employee_db where name='Vishal'":
            self._result = (123,)
        elif query == "select id from employee_db where name='Veera'":
            self._result = (789,)
        else:
            self._result = (-1,)

    def fetchone(self):
        return self._result

    def close(self):
        pass
