#include<bits/stdc++.h>
#include<mpi.h>
using namespace std;

#define N 12
int a[] = {1,2,3,4,7,9,13,24,55,56,67,88};
int key = 55;

//Temporary Array for Slave Process
int buffer[20];

int binarySearch(const int *array, int start, int end, int value) {
    int mid;
    while(start <= end) {
        mid = start + (end-start)/2;
        if(array[mid] == value)
            return mid;
        else if(array[mid] > value)
            end = mid - 1;
        else
            start = mid + 1;
    }
    return -1;
}

int main(int argc, char* argv[]) {

    int pid, np;
    MPI_Status status;

    //Initialize MPI Environment
    MPI_Init(&argc, &argv);

    //To get rank of a process
    MPI_Comm_rank(MPI_COMM_WORLD, &pid);

    //To get number of processes which are communicating
    MPI_Comm_size(MPI_COMM_WORLD, &np);

    int elements_per_process = N/np;
    int n_elements_received;

    //Master Process
    if(pid == 0) {
        int index, i;

        //Check if more than one process is running
        if(np > 1) {
            for(i=1; i<np-1; i++) {
                index = i * elements_per_process;
                //Send the number of elements to the slave process
                MPI_Send(&elements_per_process, 1, MPI_INT, i, 0, MPI_COMM_WORLD);

                //Send the actual element to the slave process
                MPI_Send(&a[index], elements_per_process, MPI_INT, i, 0, MPI_COMM_WORLD);
            }

            //For the last process
            index = i* elements_per_process;
            int elements_left = N - index;

            //Send the number of elements to the slave process
            MPI_Send(&elements_left, 1, MPI_INT, i, 0, MPI_COMM_WORLD);

            //Send the actual element to the slave process
            MPI_Send(&a[index], elements_left, MPI_INT, i, 0, MPI_COMM_WORLD);
        }

        //Master itself performs binary search
        int position = binarySearch(a, 0, elements_per_process-1, key);
        printf("pid %d: relative index = %d\n",pid,position);

        if(position != -1)
            printf("\n%d found at: %d\nby pid: 0\n\n", key, position);

        //Collect Partial Result (Search Index) from Slave Processes
        int relative_index;
        for(i=1; i<np; i++) {

            //Get Search Index from each Slave Process
            MPI_Recv(&relative_index, 1, MPI_INT, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &status);

            //Process ID of the slave process
            int sender = status.MPI_SOURCE;
            position = sender*elements_per_process+relative_index;

            //Display search index if found
            if(relative_index != -1)
                printf("\n%d found at: %d\nby pid: %d\n\n", key, position, sender);
        }
    }

        //Slave Process
    else {

        //Recieve number of elements from master process
        MPI_Recv(&n_elements_received, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);

        //Recieve the elements from master process
        MPI_Recv(&buffer, n_elements_received, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);

//        for(int i=0;i<n_elements_received;i++)
//            cout<<buffer[i]<<" ";
//        cout<<"\N";

        //Calculate the partial index
        int position = binarySearch(buffer, 0, n_elements_received-1, key);
        printf("pid %d: relative index = %d\n",pid,position);

        //Send the partial index back to the master process
        MPI_Send(&position, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }
    MPI_Finalize();

    return 0;
}

// set(CMAKE_CXX_COMPILER mpicxx)
// mpicxx binary_search_mpi.cpp
// mpirun -np 4 ./a.out