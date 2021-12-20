#include "bits/stdc++.h"
#include "omp.h"
using namespace std;

#define N 1000000

int binary_search(const int *a, int low, int high, int key) {
    int loc = -1;
    int current_thead;
    int mid;

    while (low <= high) {
        mid = (high+low)/2;
        if (a[mid] == key) {
            loc = mid;
            cout<<"found by thread: "<<current_thead<<endl;
            break;
        }
        else {
            #pragma omp parallel sections
            {
                #pragma omp section
                {
                    if (a[mid] < key) low = mid + 1;
                    current_thead = omp_get_thread_num();
                }
                #pragma omp section
                {
                    if (a[mid] > key) high = mid - 1;
                    current_thead = omp_get_thread_num();
                }
            }
        }
    }

    return loc;
}

int main() {

    int *a = new int[N];
    int offset = rand()%97;
    for(int i=0; i<N; i++) a[i]=i+offset;

    int key = 69420;

    omp_set_num_threads(8);
    double start = omp_get_wtime();
    int loc = binary_search(a, 0, N, key);
    double end = omp_get_wtime();

    if (loc==-1) cout<<key<<" not found"<<endl;
    else cout<<key<<" found at index: "<<loc<<endl;
    cout<<"time: "<<(end-start)<<endl;

    return 0;
}