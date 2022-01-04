class Boss:
    workers = []
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company

    def __repr__(self):
        return f'id:{self.id}/name:{self.name}/company:{self.company}/workers:{self.workers}'

    @property
    def boss_workers(self):
        return self.workers
    @boss_workers.setter
    def boss_workers(self, worker):
        if not worker.boss:
            self.workers.append(worker.name)
            worker.boss_worker = self


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __repr__(self):
        return f'Worker {self.name}, boss - {self.company}'

    @property
    def boss_worker(self):
        if self.boss:
            return self.boss.name
        return 'No boss'
    @boss_worker.setter
    def boss_worker(self, boss: Boss):
        self.boss = boss
        self.company = boss.company

    @boss_worker.deleter
    def boss_worker(self):
        self.boss, self.company = None, None
        Boss.workers.remove(self.name)
