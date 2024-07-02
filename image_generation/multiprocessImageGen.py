from multiprocessing import Process
import os

threads = 10

def work(t):
    print(f"Started work on {t}.")
    for _ in range(20): os.system('python3 terrainGeneration.py')
    print(f"Finished work on {t}.")

if __name__ == '__main__':
    processes = []
    for t in range(threads):
        p = Process(target=work, args=(t,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()