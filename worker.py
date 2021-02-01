from rq import Connection, Worker

from app import conn, queue,enqueue_jobs_init

if __name__ == "__main__":
    with Connection(conn):
        w = Worker([queue])
        w.work()
    enqueue_jobs_init()
        