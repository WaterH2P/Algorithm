#include<bits/stdc++.h>
using namespace std;
char position(long long int pos)
{
    if(pos<6)
    {
        ostringstream s;
        s<<pos;
        string temp = s.str();
        return temp[0];
    }
    long long int breakpoint = 6;
    long long int prevbreakpoint = 1;
    long long int present  = 1;
    char prev = '1';
    char presentchar = '5';
    while(1)
    {
        prevbreakpoint = breakpoint;
        breakpoint = 2*(breakpoint-1) + present + 1;
        if(breakpoint > pos)
            break;
        present++;
        prev = presentchar;
        presentchar = '1';
    }
    if(pos<=(prevbreakpoint+(present-1)) && pos>=prevbreakpoint)
    {
        return '$';
    }
    else
    {
        long long int total = 2*(prevbreakpoint-1)+present;
        return position((total-pos)+1);
    }
}
int main()
 {
	int testcases;
	cin>>testcases;
	vector<char> ans;
	for(int i=0;i<testcases;i++)
	{
	    long long int pos;
	    cin>>pos;
	    ans.push_back(position(pos));
	}
	for(auto x : ans)
	{
	    if(x=='0')
	        cout<<endl;
	    else
	        cout<<x<<endl;
	}
	return 0;
}