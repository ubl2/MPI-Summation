from mpi4py import MPI
import math
import numpy as np

#initialize MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sum_final=0
work_array = np.array(range(4,404,1))
buffer_size = math.floor(len(work_array)/size)

if rank == 0:
    #temp variables: buffer indices for worker chunks
    start_index = 0
    stop_index = 0

    #one-dimensional arrays for reporting local sums
    root_local_sum = np.array(0, dtype='int')
    worker_local_sum = np.array(0, dtype='int')

    #chuck size for distributing work to all 
    local_array = np.zeros(buffer_size, dtype='int')

    #First chunk is for Master. Take it and calculate local sum. 
    local_array = work_array[0:buffer_size]
    sum=0
    for i in local_array:
        sum=sum+i
    root_local_sum=sum
    print("Master calculated integer sum is",root_local_sum)
    #Prepare indices and send chunk to all wokers with rank > 0
    for j in range(size-1):
        j=j+1
        start_index = j*buffer_size
        stop_index = (j+1)*buffer_size
        local_array = work_array[start_index:stop_index]
        #Send Work to wokers 
        comm.Send(local_array,dest=j)
    
        #Receive Results: Each worker adds all integers and send results.
        comm.Recv([worker_local_sum, MPI.INT], source=j, tag=0)
        sum_final=sum_final+worker_local_sum
else:
    #local array to hold data received from Master
    local_array = np.zeros(buffer_size, dtype='int')
    #variable that stores sum of integers in local_array
    worker_sum = np.array(0, dtype='int')

    #Receive Work from Master: This will be the part of the array send by Master to the Worker
    comm.Recv(local_array,source=0, tag=0)
    #print(local_array, rank,"/n")
    sum=0
    for i in local_array:
        sum=sum+i
    worker_sum=sum
    print ("Received integer sum of ",worker_sum, "from worker of rank",rank)
    #send local sum to master
    comm.Send(worker_sum,dest=0) 
