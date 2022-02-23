#include<bits/stdc++.h>
using namespace std;


int main()
{
    int n;
    cin>>n;
    vector<int>v(n);
    string s = "p";
    string t[4] = {"p4","p2","p3","p1"};

    for(int i=0; i<n; i++){
        cin>>v[i];
    }

    sort(v.begin(),v.end());

    int sum=0,temp=0,cnt=0;

    for(int i=0; i<n; i++){

        cnt++;
        cout<<temp<<' '<<t[i]<<' ';
        temp += v[i];
        if(cnt<n){
           sum += temp;
        }
    }
    cout<<temp<<endl;
    cout<<setprecision(2)<<fixed<<"avg "<<(float)sum/n<<endl;




    return 0;
}
