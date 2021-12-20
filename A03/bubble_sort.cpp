#include "bits/stdc++.h"
#include "omp.h"
using namespace std;

#define N 1024
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int *a = new int[N];
    for(int i=0; i < N; i++) a[i]=rand()%N;

    cout<<"initial array:\n";
    for(int i=0; i < N; i++) cout<<a[i]<<" ";
    cout<<endl;

    int i=0, j=0,first=0;
    double start, end;

    omp_set_num_threads(4);
    start = omp_get_wtime();
    for(i=0; i<N-1; i++) {
        first = i%2;
        #pragma omp parallel for
        for(j=first; j<N-1; j++) {
            if(a[j] > a[j+1])
              swap(&a[j], &a[j+1]);
        }
    }
    end = omp_get_wtime();

    cout<<"sorted array:\n";
    for(i=0; i < N; i++) cout<<a[i]<<" ";
    cout<<endl;

    cout<<"time: "<<(end-start)<<endl;

    return 0;
}