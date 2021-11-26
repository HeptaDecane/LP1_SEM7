#include "iostream"

__global__ void cuda_hello(){
    printf("Hello from block %d, thread %d\n", blockIdx.x, threadIdx.x);
}


int main(){
    printf("Hello World!\n");
    cuda_hello<<<4,8>>>();
    cudaDeviceSynchronize();
    return 0;
}