#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int N, x, y;
    set <int> lfc;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> y >> x;
        if(y==1)
            lfc.insert(x);
        else if(y==2){
            if (lfc.find(x) != lfc.end())
                lfc.erase(x);    }
        else if(y==3 && lfc.find(x) != lfc.end())
            cout << "Yes" << endl;
        else if(lfc.find(x) == lfc.end())
            cout << "No" << endl;
    }
    return 0;
}



