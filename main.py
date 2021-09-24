from threading import Thread, Semaphore
import time
import random       

queue = []         #queue from where producer will produce data and consumer will consume data
MAX_NUM = 10       #max limit of the queue

sem = Semaphore()  #intitializing semaphore

class ProducerThread(Thread):
    def run(self):
        nums = range(5) # [0 1 2 3 4]
        global queue
        
        while True:
            sem.acquire()  #wait operation to stop consuming 
            if len(queue) == MAX_NUM:
                
                print ("Lista está cheia, Prudutor vai aguardar o Consumidor;")
                sem.release() #signal operation only when when queue is full and allow consumer to consume data
                print ("Espaço liberado no buffer, Consumidor notificou o produtor")

            num = random.choice(nums) 
            queue.append(num) #added any random number from 0 to 4 to the list
            print ("Produzido", num) 
            sem.release() #signal operation to allow consumer to consume data

            time.sleep(random.random()) #to allow program to run a bit slower 

class ConsumerThread(Thread):
    def run(self):
        global queue
        
        while True:
            sem.acquire()   #wait operation to stop producing
            if not queue:
                print ("Lista está vazia, Consumidor está aguardando Produtor;")
                sem.release()  #signal operation only when when queue is empty and allow producer to produce data
                print ("Produtor inseriu algo no buffer e notificou o Consumidor")
            else:
                num = queue.pop(0)
                print ("Consumido", num)
                
            sem.release()  #signal operation to allow producer to produce

            time.sleep(random.random())

def main():
    ProducerThread().start()    #start producer thread
    ConsumerThread().start()    #start consumer thread


if __name__ == '__main__':
    main()