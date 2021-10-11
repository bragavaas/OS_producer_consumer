from threading import Thread, Semaphore
import time
import random       

processReadyQueue = []
processWaitingQueue = []
MAX_NUM = 100       

sem = Semaphore()  

class Process:
    def __init__(self):
        self.Process_ID = "[PID]"+str(random.randrange(1000, 9999)) #Valores inteiros E ÚNICOS de 5 dígitos
        self.Process_State = 'READY'
        self.Process_Blocked = False
        self.Process_WaitTime = 0
        self.Process_executeAgain = False

    def changeState(self, state):
        self.Process_State = state 
        self.randomExecuteAgain()  # A cada mudança de estado, verifica se o processo será repetido. Caso verdadeiro, volta para lista de processos disponíveis.
        if state == 'BLOCKED': # A cada mudança de estado, verifica se o estado é bloqueado, se for, gera um tempo novo de espera
            self.Process_WaitTime = random.randrange(100, 4000, 100) #Numero aleatorio com piso em 100, teto em 4000 e saltos de 100 em 100
        
    def randomExecuteAgain(self): 
        self.Process_executeAgain = bool(random.getrandbits(1))

    def randomState(self):
        self.Process_Blocked = bool(random.getrandbits(1))

class ReadyQueueHandler(Thread):
    def run(self):
        global processReadyQueue
        
        while True:
            sem.acquire()  
            if len(processReadyQueue) == MAX_NUM:
                #print ("[THREAD 1] Lista de Processos disponíveis está cheia. Aguardando liberação de processos.")
                sem.release() 
            processReadyQueue.append( Process() )
            processoLista = processReadyQueue[-1]
            print ("[THREAD 1] Processo " +processoLista.Process_ID+ " acrescentado na última posição da lista de Processos Disponíveis.") 
            sem.release() 

            time.sleep(random.random()) 

class WaitingQueueHandler(Thread):
    def run(self):
        global processWaitingQueue
        
        while True:
            sem.acquire()   
            if not processWaitingQueue:
                #print ("[THREAD 2] Lista de Processos em Espera está Vazia. Aguardando Processos...")
                sem.release() 
            else:
                Process = processWaitingQueue[0]
                print ("[THREAD 2] Processo " +Process.Process_ID+ " está na fila de espera. Aguardando seu tempo de espera de " +Process.Process_WaitTime+" milisegundos") 
                time.sleep(Process.Process_WaitTime)
                
            sem.release() 
            time.sleep(random.random())

class ProcessExecution(Thread):
    def run(self):
        global processReadyQueue
        
        while True:
            sem.acquire()   
            if not processReadyQueue:
                #print ("[THREAD 3] A Lista de Processos está vazia. Aguardando Processos para executar...")
                sem.release() 
            else:
                Process = processReadyQueue[0]
                Process.changeState("RUNNING")

                if Process.Process_Blocked == True:
                    print ("[THREAD 3] O Processo está bloqueado, movendo-o para lista de espera.")
                    Process.changeState("BLOCKED")
                    processWaitingQueue.append(Process)
                    
                else:
                    if Process.Process_executeAgain == True:
                        print ("[THREAD 3] O Processo Executará novamente, vamos adiciona-lo no final da lista de Processos Disponíveis.")
                        processReadyQueue.append(Process)
                    else:
                        print ("[THREAD 3] O Processo Terminou.")
                        Process.changeState("TERMINATED")
                        del Process

                processReadyQueue.pop(0)
 
            sem.release()  

            time.sleep(random.random())

def main():
    ReadyQueueHandler().start()    #THREAD 1
    WaitingQueueHandler().start()  #THREAD 2
    ProcessExecution().start()     #THREAD 3

if __name__ == '__main__':
    main()