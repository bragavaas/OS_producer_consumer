from threading import Thread, Semaphore
import time
import random 


buffer = []
MAX_NUM = 10 

class ProducerThread(Thread):
    def run(self):
        nums = range(5) #generate random numbers 1 to 5
        global buffer

        while True:
            if len(buffer) == MAX_NUM:
                print("Lista está cheia, o produtor aguardará o consumidor;")

            num = random.choice(nums)
            buffer.append(num) #adicionou o numero aleatório no buffer
            print("Produzido", num)

            time.sleep(random.random()) #para o programa exuctar um pouco mais devagar e permitir a visualização


class ConsumerThread(Thread):
    def run(self):
        global buffer

        while True:
            if not buffer:
                print("Lista está vazia, aguardando Produtor;")
            else:
                num = buffer.pop(0)
                print("Consumido", num)  
            time.sleep(random.random()) #para o programa exuctar um pouco mais devagar e permitir a visualização


def main():
    ProducerThread().start()    #inicia thread Produtor
    ConsumerThread().start()    #inicia thread Consumidor

if __name__ == '__main__':
    main()