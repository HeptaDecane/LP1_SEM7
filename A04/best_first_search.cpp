#include<bits/stdc++.h>
#include "omp.h"
using namespace std;

#define N 7

list<int> q;
vector<int> weight(N, 1000);
bool *visited = new bool[N]{false};

struct Comparator {
    // Compare 2 Edges objects using weight
    bool operator ()(const int &e1, const int &e2){
        return weight[e1]<weight[e2];
    }
};

void best_first_search(int adj_matrix[N][N])
{
    if(q.empty()) return;
    q.sort(Comparator());

    //pop first element and display it
    int current_node = q.front();
    q.pop_front();
    cout<<current_node<<", ";

    //For every element in the row of the adjacency matrix
    #pragma omp parallel for shared(visited,q,weight)
    for(int i=0; i<N; i++){
        //If an unvisited Edge exists
        if(adj_matrix[current_node][i] > 0 && !visited[i]){

            //Replace the weight if it is larger
            if(weight[i] > adj_matrix[current_node][i])
                weight[i] = adj_matrix[current_node][i];

            //Push the destination of the smallest edge onto the queue
            q.push_back(i);
            visited[i]=true;
        }
    }

    //Call the function recursively
    best_first_search(adj_matrix);
}

int main(){
    //Set the Adjacency Matrix
    int adj_matrix[N][N] = {
            {0	,10  ,15  ,0  ,0  ,0  ,0},
            {10	,0	,25	,25	,0	,0	,0},
            {15	,25	,0	,0	,40	,0	,0},
            {0	,25	,0	,0	,20	,0	,0},
            {0	,0	,40	,20	,0	,5	,0},
            {0	,0	,0	,0	,5	,0	,20},
            {0	,0	,0	,0	,0	,20	,0}
    };

    int start_node = 3;
    q.push_back(start_node);
    weight[start_node] = 0;
    visited[start_node] = true;

    omp_set_num_threads(8);
    double start = omp_get_wtime();
    best_first_search(adj_matrix);
    double end = omp_get_wtime();
    cout<<endl;
    cout<<"time: "<<(end-start)<<endl;

    return 0;
}