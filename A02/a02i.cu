#include "bits/stdc++.h"
using namespace std;

#define N 8
size_t bytes;

__global__ void vector_addition(int *a, int *b, int *c, int n){
    unsigned int idx = blockDim.x * blockIdx.x + threadIdx.x;
    if(idx < n)
        c[idx] = a[idx] + b[idx];
}

int main() {
    int *a = new int[N];
    cout<<"a: ";
    for(int i=0; i<N; i++){
        a[i] = rand()%97;
        cout<<a[i]<<" ";
    }
    cout<<endl;

    int *b = new int[N];
    cout<<"b: ";
    for(int i=0; i<N; i++){
        b[i] = rand()%97;
        cout<<b[i]<<" ";
    }
    cout<<endl;

    bytes = N*sizeof(int);

    int *d_a;
    cudaMalloc(&d_a, bytes);
    cudaMemcpy(d_a, a, bytes, cudaMemcpyHostToDevice);

    int *d_b;
    cudaMalloc(&d_b, bytes);
    cudaMemcpy(d_b, b, bytes, cudaMemcpyHostToDevice);

    int *c = new int[N]{0};
    int *d_c;
    cudaMalloc(&d_c, bytes);

    int threads = 64;
    int blocks = ceil(float(N)/float(threads));

    vector_addition<<<blocks,threads>>>(d_a, d_b, d_c, N);
    cudaDeviceSynchronize();
    cudaMemcpy(c, d_c, bytes, cudaMemcpyDeviceToHost);

    cout<<"c: ";
    for(int i=0; i<N; i++) cout<<c[i]<<" ";
    cout<<endl;

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;
}
