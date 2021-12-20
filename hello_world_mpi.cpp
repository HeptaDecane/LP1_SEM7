#include "bits/stdc++.h"
#include "mpi.h"
using namespace std;

int main(int argc, char* argv[]) {
    int pid, np;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &pid);
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    printf("Hello World! (%d/%d)\n",pid,np);
    MPI_Finalize();

    return 0;
}

// mpicxx hello_world_mpi.cpp
// mpirun -np 8 ./a.out