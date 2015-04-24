from multiprocessing import Process, Queue, Pipe

def func(queue):
    queue.put(["hello world",1,1,1,1])

def pipe(conn):
    conn.send([42, None, 'hello world'])
    conn.close()



if __name__ == "__main__":
    queue = Queue()
    p = Process(target=func, args=(queue,))
    p.start()
    print queue.get()
    p.join()
    print "+++++++++++"
    parent_conn, child_conn = Pipe()
    p = Process(target=pipe, args=(child_conn,))
    p.start()
    print parent_conn.recv()
    p.join()
