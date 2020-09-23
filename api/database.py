from api.models import Task
import uuid

class DBSession:
    tasks = {}
    def __init__(self):
        self.tasks = DBSession.tasks
    def read_all_task(self):
        return self.tasks

    def read_one_task(self, id):
        return self.tasks[id]

    def add_task(self, valor: Task):
        id = uuid.uuid4()
        self.tasks[id] = valor
        return id

    def replace_task(self, id, valor: Task):
        self.tasks[id]=valor 

    def del_task(self, id):
        del self.tasks[id]

    def modify_task(self,id,valor: Task):
        self.tasks[id] = self.taks[id].copy(update=valor.dict(exclude_unset=True))

def get_db():
    return DBSession()