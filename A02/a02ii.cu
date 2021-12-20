#include "bits/stdc++.h"
using namespace std;

#define N 8
#define M 4
size_t bytes;

// 1xN * NxM = 1xM
__global__ void vecmat_multiplication(int* vector, int* matrix, int* result, int n, int m){
    unsigned int idx = blockDim.x * blockIdx.x + threadIdx.x;
    if(idx < m){
        int sum = 0;
        for(int i=0; i<n; i++)
            sum += vector[i]*matrix[i*m+idx];

        result[idx] = sum;
    }
}

void print_grid(int* array, int n, int m){
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++)
            cout<<array[i*m+j]<<" ";
        cout<<endl;
    }
    cout<<endl;
}

int main() {
    int *vector = new int[N];
    for(int i=0; i<N; i++)
        vector[i] = rand()%97;

    int *matrix = new int[N*M];
    for(int i=0; i<N*M; i++)
        matrix[i] = rand()%97;

    cout<<"vector:"<<endl;
    print_grid(vector, 1, N);

    cout<<"matrix:"<<endl;
    print_grid(matrix, N, M);

    int *d_vector;
    bytes = N*sizeof(int);
    cudaMalloc(&d_vector, bytes);
    cudaMemcpy(d_vector, vector, bytes, cudaMemcpyHostToDevice);

    int *d_matrix;
    bytes = N*M*sizeof(int);
    cudaMalloc(&d_matrix, bytes);
    cudaMemcpy(d_matrix, matrix, bytes, cudaMemcpyHostToDevice);

    int *result = new int[M]{0};
    int *d_result;
    bytes = M*sizeof(int);
    cudaMalloc(&d_result, bytes);

    int threads = 64;
    int blocks = ceil(float(M)/float(threads));

    vecmat_multiplication<<<blocks,threads>>>(d_vector, d_matrix, d_result, N, M);
    cudaDeviceSynchronize();

    bytes = M*sizeof(int);
    cudaMemcpy(result, d_result, bytes, cudaMemcpyDeviceToHost);

    cout<<"result:"<<endl;
    print_grid(result, 1, M);

    cudaFree(d_vector);
    cudaFree(d_matrix);
    cudaFree(d_result);
    return 0;
}
