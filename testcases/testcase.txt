#include<bits/stdc++.h>
using namespace std;
int main()
{
vector<int> v;
int n,temp;
cin>>n;
for(int e=0;e<n;e++){
cin>>temp;
v.push_back(temp);
}
map<int,int> mp;
for(int e:v) mp[e]++;
cout<<"Frequency Distribution is given below as Value: Frequency\n";
for(auto it:mp){
cout<<it.first<<" "<<it.second<<endl;
}
return 0;
}
