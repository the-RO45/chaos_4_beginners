#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <queue>
#include <sstream>
#include <typeinfo>
#include <bits/stdc++.h>
using namespace std;
 
int securitiesBuying(int z,int security_value[],int n)
{
    int no_of_stocks=0;
   // participants code here
    map<int,int> price_count_map;
    for(int i=0;i<n;i++)
    {
        price_count_map.insert({security_value[i],i+1});
    }
    
    for(auto a : price_count_map)
    {
        if(z>= (a.first * a.second))
        {
            z = z - (a.first * a.second);
            no_of_stocks += a.second;
        }
        else
        {
            no_of_stocks+= z / (a.first);
            break;
        }
    }
    
    return no_of_stocks;
}
 
int main(){
 
int z;
cin>>z;
vector<int> input_data;
string buffer;
int data;
getline(cin, buffer);
getline(cin, buffer);
istringstream iss(buffer);
 
 
while (iss >> data)
    input_data.push_back(data);
 
int n= input_data.size();
 
 
 int security_value[n];
    for (int i = 0; i < n; i++) {
        security_value[i] = input_data[i];
    }
 
 
 
int no_of_stocks_purchased = securitiesBuying(z,security_value,n);
cout << no_of_stocks_purchased;
 
 
 
}
 
 
