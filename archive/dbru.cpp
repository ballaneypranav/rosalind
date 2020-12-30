#include <iostream>
#include <fstream>
#include <set>

using namespace std;

string rc(string s);

int main(void)
{
    string line;
    ifstream file("rosalind_dbru.txt");

    set<string> S, Src, S_union_Src;

    while (getline(file, line))
    {
        S.insert(line);
        S_union_Src.insert(line);
    }

    for (auto x : S)
    {
        string reverse_complement = rc(x);
        Src.insert(reverse_complement);
        S_union_Src.insert(reverse_complement);
    }

    // for (auto x: S_union_Src)
    //     cout << x << "\n";

    set<pair<string, string>> DBG;

    for (auto x: S_union_Src)
    {
        int len = x.length();
        string a = x.substr(0, len-1);
        string b = x.substr(1, len-1);
        cout << '(' << a << ", " << b << ")\n";
    }    
}

string rc(string s)
{
    string reverse_complement = "";
    for (int i = s.length() - 1; i >= 0; i--)
    {
        switch (s[i])
        {
        case 'A':
            reverse_complement.append("T");
            break;
        case 'T':
            reverse_complement.append("A");
            break;
        case 'G':
            reverse_complement.append("C");
            break;
        case 'C':
            reverse_complement.append("G");
            break;
        }
    }
    return reverse_complement;
}