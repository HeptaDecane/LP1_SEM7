#include "bits/stdc++.h"
using namespace std;

#define N 8
size_t bytes;

__global__ void min(double *array, int n) {
    unsigned int id = blockDim.x * blockIdx.x + threadIdx.x;
    int step_size = 1;

    while(n > 0) {
        if(id < n) {
            int i = (int)id * step_size * 2;
            int j = i + step_size;
            if(array[i] > array[j])
                array[i] = array[j];
        }
        step_size = step_size*2;
        n = n/2;
    }
}

__global__ void max(double *array, int n) {
    unsigned int id = blockDim.x * blockIdx.x + threadIdx.x;
    int step_size = 1;

    while(n > 0) {
        if(id < n) {
            int i = (int)id * step_size * 2;
            int j = i + step_size;
            if(array[i] < array[j])
                array[i] = array[j];
        }
        step_size = step_size*2;
        n = n/2;
    }
}


__global__ void sum(double *array, int n) {
    unsigned int id = blockDim.x * blockIdx.x + threadIdx.x;
    int step_size = 1;

    while(n > 0) {
        if(id < n) {
            int i = (int)id * step_size * 2;
            int j = i + step_size;
            array[i] = array[i] + array[j];
        }
        step_size = step_size*2;
        n = n/2;
    }
}

__global__ void mean_diff_square(double* array, double avg, int n){
    unsigned int id = blockDim.x * blockIdx.x + threadIdx.x;
    if(id < n)
        array[id] = (array[id]-avg)*(array[id]-avg);
}

int main() {
    double *array = new double [N];
    cout<<"array: ";
    for(int i=0; i<N; i++){
        array[i] = rand()%97;
        cout<<array[i]<<" ";
    }
    cout<<endl;

    double result;
    double *d_array;
    bytes = N*sizeof(double); //calculate no. of bytes for array
    cudaMalloc(&d_array, bytes);

    //MIN
    cudaMemcpy(d_array, array, bytes, cudaMemcpyHostToDevice);
    min<<<1,N/2>>>(d_array,N/2);
    cudaDeviceSynchronize();
    cudaMemcpy(&result, d_array, sizeof(double), cudaMemcpyDeviceToHost);
    cout<<"min: "<<result<<endl;

    //MAX
    cudaMemcpy(d_array, array, bytes, cudaMemcpyHostToDevice);
    max<<<1,N/2>>>(d_array, N/2);
    cudaDeviceSynchronize();
    cudaMemcpy(&result, d_array, sizeof(double), cudaMemcpyDeviceToHost);
    cout<<"max: "<<result<<endl;

    //SUM
    cudaMemcpy(d_array, array, bytes, cudaMemcpyHostToDevice);
    sum<<<1,N/2>>>(d_array,N/2);
    cudaDeviceSynchronize();
    cudaMemcpy(&result, d_array, sizeof(double), cudaMemcpyDeviceToHost);
    cout<<"sum: "<<result<<endl;

    //AVG
    double avg = result/N;
    cout<<"avg: "<<avg<<endl;

    //STD
    cudaMemcpy(d_array, array, bytes, cudaMemcpyHostToDevice);
    mean_diff_square<<<1,N>>>(d_array, avg, N);
    cudaDeviceSynchronize();
    sum<<<1,N/2>>>(d_array,N/2);
    cudaDeviceSynchronize();
    cudaMemcpy(&result, d_array, sizeof(double), cudaMemcpyDeviceToHost);
    double variance = result/N;
    cout<<"std: "<<sqrt(variance)<<endl;

    cudaFree(d_array);
    return 0;
}
