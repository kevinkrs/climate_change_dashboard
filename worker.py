from rq import Connection, Worker

from app import conn, queue

if __name__ == "__main__":
    with Connection(conn):
        w = Worker([queue])
        w.work()

        