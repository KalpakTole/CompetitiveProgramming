//
// Author: Arsh
// Username: arsh_16
// Created On: 25-02-2021 at 10:15 AM
//

#include <bits/stdc++.h>
#include <fstream>
using namespace std;

#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;

const int MOD = 1e9+7;

template <typename A, typename B>
string to_string(pair<A, B> p);

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p);

template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p);

string to_string(const string& s) {
    return '"' + s + '"';
}

string to_string(const char* s) {
    return to_string((string) s);
}

string to_string(bool b) {
    return (b ? "true" : "false");
}

string to_string(char c){
    return string(1, c);
}

string to_string(vector<bool> v) {
    bool first = true;
    string res = "{";
    for (int i = 0; i < static_cast<int>(v.size()); i++) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(v[i]);
    }
    res += "}";
    return res;
}

template <size_t N>
string to_string(bitset<N> v) {
    string res = "";
    for (size_t i = 0; i < N; i++) {
        res += static_cast<char>('0' + v[i]);
    }
    return res;
}

template <typename A>
string to_string(A v) {
    bool first = true;
    string res = "{";
    for (const auto &x : v) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
    }
    res += "}";
    return res;
}

template <typename A>
void debug_pq(A v) {
    bool first = true;
    string res = "{";
    while (!v.empty()){
        auto x = v.top();
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
        v.pop();
    }
    res += "}";
    cerr << res << "\n";
}

template <typename A>
void debug_que(A v) {
    bool first = true;
    string res = "{";
    while (!v.empty()){
        auto x = v.front();
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
        v.pop();
    }
    res += "}";
    cerr << res << "\n";
}


template <typename A, typename B>
string to_string(pair<A, B> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";
}

template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ", " + to_string(get<3>(p)) + ")";
}


void debug_out() { cerr << endl; }

template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
    cerr << " " << to_string(H);
    debug_out(T...);
}

#define LOCAL

#ifdef LOCAL
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif


ifstream  ifile;
ofstream  ofile;
const string path = "C:\\Users\\kalpa\\Desktop\\Kalpak\\Codechef";
string  ifname, opfname;

int D, I, V, S, F;


void setup(string fname){
    ifname = path+fname+".txt";
    opfname = path+fname+ "_out.txt";
    ifile.open(ifname);
    ofile.open(opfname);
}

void close_files(){
    ifile.close();
    ofile.close();
}

struct node{
    int to;
    string name;
    int dur;
};
vector<vector<node>> inter;
vector<vector<string>> carpaths;

int main(){
//    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    setup("a");

    ifile >> D >> I >> S >> V >> F;

    debug(D, I, S, V, F);
    inter.resize(I);
    carpaths.resize(V);
    for (int i=0; i<S; i++){
        int src, dest, dur;
        string sname;
        ifile >> dest >> src >> sname >> dur;

        debug(src, dest, sname, dur);
        node cur;
        cur.to = dest;
        cur.name = sname;
        cur.dur = dur;
        inter[src].emplace_back(cur);
    }

    for (int i=0; i<V; i++){
        int len;
        ifile >> len;
        debug(i, len);
        for (int j=0; j<len; j++){
            string cur;
            ifile >> cur;
            debug(cur);
            carpaths[i].emplace_back(cur);
        }
    }

    ofile << I << "\n";
    for (int i=0; i<I; i++){
        ofile << i <<"\n";
        ofile << inter[i].size() << "\n";
        for (int j=0; j<inter[i].size(); j++)
            ofile << inter[i][j].name << " " << 1 << "\n";
    }



    close_files();
}