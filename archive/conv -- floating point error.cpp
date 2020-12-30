#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <unordered_map>

using namespace std;

unordered_map<float, int> get_floats(string line);
void minkowski_diff(unordered_map<float, int> S1, unordered_map<float, int> S2);
unordered_map<float, int>::iterator find_approx(float f);

unordered_map<float, int> MD;

int main(void)
{
    string line;
    ifstream file("rosalind_conv.txt");

    getline(file, line);
    unordered_map<float, int> S1 = get_floats(line);
    getline(file, line);
    unordered_map<float, int> S2 = get_floats(line);

    minkowski_diff(S1, S2);

    int max_multiplicity = 0;
    float x;
    for(auto itr = MD.begin(); itr != MD.end(); ++itr)
    {
        if (itr->second > max_multiplicity)
        {
            max_multiplicity = itr->second;
            x = itr->first;
        }
    }

    cout << fixed;
    cout << setprecision(5);
    cout << max_multiplicity << "\n" << x;
}

unordered_map<float, int> get_floats(string line)
{
    unordered_map<float, int> S;
    istringstream ss(line);
    string word;
    while (ss >> word)
    {
        float current = stof(word);
        unordered_map<float, int>::iterator itr = S.find(current);
        if (itr != S.end())
        {
            itr->second += 1;
        }
        else
            S.insert(pair<float, int>(current, 1));
    }

    return S;
}

void minkowski_diff(unordered_map<float, int> S1, unordered_map<float, int> S2) 
{
    for (auto s1 : S1)
    {
        for (auto s2: S2)
        {
            float diff = s1.first - s2.first;
            auto ptr = find_approx(diff);
            if (ptr != MD.end())
                ptr->second += s1.second * s2.second;
            else
                MD.insert(pair<float, int>(diff, s1.second * s2.second));
        }
    }
}


unordered_map<float, int>::iterator find_approx(float f) 
{
    unordered_map<float, int>::iterator itr;
    for(itr = MD.begin(); itr != MD.end(); ++itr)
        if (abs(itr->first - f) < 0.00001)
            break;
    
    return itr;
}