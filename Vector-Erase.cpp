#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
using namespace std;


int main() {
    int N, temp, a, b, c;
    vector<int> vec;
    cin >> N;
    for(int i=0;i<N;i++){
        cin >> temp;
        vec.push_back(temp);
    }

    cin >> a >> b >> c;
    vec.erase(vec.begin()+a-1);
    vec.erase(vec.begin()+b-1, vec.begin()+c-1);
    cout << vec.size() << endl;
    for(int i=0;i<vec.size();i++){
        cout << vec[i] << ' ';
    }
    return 0;
}

