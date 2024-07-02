from multiprocessing import Process
import os

THREADS = 10 # Don't use green threads, use real cores (hyperthreading counts as real cores).
IMAGES_PER_THREAD = 20

def work(t):
    print(f"Started work on {t}.")
    for _ in range(IMAGES_PER_THREAD): os.system('python3 terrainGeneration.py')
    print(f"Finished work on {t}.")

if __name__ == '__main__':
    processes = []
    print(f"Amount to generate: {THREADS * IMAGES_PER_THREAD}.")
    for t in range(THREADS):
        p = Process(target=work, args=(t,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print("Done.")