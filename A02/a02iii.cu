#include "bits/stdc++.h"
using namespace std;

#define M 8
#define N 8
#define K 8
size_t bytes;

// MxN * NxK = MxK
__global__ void matrix_multiplication(int *a, int *b, int *c, int m, int n, int k){
    unsigned int row = blockIdx.y * blockIdx.y + threadIdx.y;
    unsigned int col = blockIdx.x * blockIdx.x + threadIdx.x;
    if(row<m && col<n){
        int sum = 0;
        for(int i=0; i<n; i++)
            sum += a[row*n+i] * b[i*k+col];

        c[row * k + col] = sum;
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
    int *a = new int[M*N];
    for(int i=0; i<M*N; i++)
        a[i] = rand()%97;

    int *b = new int[N*K];
    for(int i=0; i<N*K; i++)
        b[i] = rand()%97;

    cout<<"a:"<<endl;
    print_grid(a,M,N);

    cout<<"b:"<<endl;
    print_grid(b,N,K);

    int *d_a;
    bytes = M*N*sizeof(int);
    cudaMalloc(&d_a, bytes);
    cudaMemcpy(d_a, a, bytes, cudaMemcpyHostToDevice);

    int *d_b;
    bytes = N*K*sizeof(int);
    cudaMalloc(&d_b, bytes);
    cudaMemcpy(d_b, b, bytes, cudaMemcpyHostToDevice);

    int *c = new int[M*K]{0};
    int* d_c;
    bytes = M*K*sizeof(int);
    cudaMalloc(&d_c, bytes);

    unsigned int block_size = 32;
    unsigned int grid_size = ceil(max(M,K)*N/float(block_size));
    dim3 dim_grid(grid_size, grid_size);
    dim3 dim_block(block_size, block_size);

    matrix_multiplication<<<dim_grid,dim_block>>>(d_a, d_b, d_c, M, N ,K);
    cudaDeviceSynchronize();

    bytes = M*K*sizeof(int);
    cudaMemcpy(c, d_c, bytes, cudaMemcpyDeviceToHost);

    cout<<"result:"<<endl;
    print_grid(c,M,K);

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;
}
