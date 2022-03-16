#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int Q, type, score;
    string name;
    map<string, int> m;
    cin >> Q;
    for(int i=0;i<Q;i++){
        cin >> type >> name;
        if(type==1){
            cin >> score;

            if(m.find(name) == m.end()) {
                m.insert(make_pair(name,score)); }
            else{
                m[name] += score; } }

        else if(type==2)
            m.erase(name);
        else if(type==3){
            if(m.find(name) == m.end()) {
                cout << 0 << endl; }
            else {
                cout << m[name] << endl; }
        }
    }
    return 0;
}



