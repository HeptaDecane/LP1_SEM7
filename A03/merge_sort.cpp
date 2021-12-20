#include "bits/stdc++.h"
#include "omp.h"
using namespace std;

#define N 1024

void merge(int* arr, int start, int mid, int end) {
    int len = (end - start) + 1;
    int temp[len];
    int cur = 0;

    int i = start;
    int j = mid + 1;
    while(i <= mid && j <= end){
        if(arr[i] < arr[j]) {
            temp[cur] = arr[i];
            cur++;
            i++;
        }
        else {
            temp[cur] = arr[j];
            cur++;
            j++;
        }
    }
    if(i <= mid) {
        while(i <= mid) {
            temp[cur] = arr[i];
            i++;
            cur++;
        }
    }

    else if(j <= end) {
        while(j <= end) {
            temp[cur] = arr[j];
            j++;
            cur++;
        }
    }

    cur = 0;
    for(i=start; i<=end; i++) {
        arr[i] = temp[cur];
        cur++;
    }

}

void mergeSort(int *arr, int start, int end) {
    if(start < end) {
        int mid = (start+end) / 2;

        #pragma omp parallel sections
        {
            #pragma omp section
            mergeSort(arr, start, mid);

            #pragma omp section
            mergeSort(arr, mid+1, end);
        }

        merge(arr, start, mid, end);
    }
}

int main() {
    int *a = new int[N];
    for(int i=0; i < N; i++) a[i]=rand()%N;

    cout<<"initial array:\n";
    for(int i=0; i < N; i++) cout<<a[i]<<" ";
    cout<<endl;

    double start, end;

    omp_set_num_threads(4);
    start = omp_get_wtime();
    mergeSort(a, 0, N-1);
    end = omp_get_wtime();

    cout<<"sorted array:\n";
    for(int i=0; i < N; i++) cout<<a[i]<<" ";
    cout<<endl;

    cout<<"Time parallel = "<<(end-start)<<endl;

    return 0;
}