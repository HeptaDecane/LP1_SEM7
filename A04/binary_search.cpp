#include<iostream>

#include<omp.h>

#include<time.h>

using namespace std;
int c1[3];
int binary_search(int a[], int low, int high, int key) {
    int loc = -1;
    int mid;
    while (low <= high) {
        mid = (high + low) / 2;
        if (a[mid] == key) {
            loc = mid;
            break;
        } 
        else {
            #pragma omp parallel sections 
            {
                //cout<<omp_get_thread_num();
                #pragma omp section 
                {
                    if (a[mid] < key) {
                        low = mid + 1;
                    }
                }
                #pragma omp section 
                {
                    if (a[mid] > key) {
                        high = mid - 1;
                    }
                }
            }
        }
    }
    return loc;
}
int main() {
    int th = omp_get_max_threads();
    cout << "Max Threads : " << th << endl;
    omp_set_num_threads(2);
    c1[1] = 0;
    c1[2] = 0;
    int a[1000000];
    clock_t t1, t2;
    int key = 0;
    int loc, i;
    for (int i = 0; i < 1000000; i++) {
        a[i] = i;
    }
    key = 1000;
    t1 = clock();
    loc = binary_search(a, 0, 1000000, key);
    t2 = clock();
    if (loc == -1) {
        cout << "Not Found";
    } else {
        cout << "Found at " << loc << endl;
        //cout<<"By Thread "<<omp_get_thread_num()<<endl;
    }
    return 0;
}