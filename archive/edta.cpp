#include <iostream>
#include <fstream>
#include <tuple>
#include <map>

using namespace std;

tuple<string, string, int> calculate_edits(string s, string t);
map<pair<string, string>, tuple<string, string, int>> calculated_results;

int main(void)
{
    string s, t;
    ifstream file("rosalind_edta.txt");

    getline(file, s);
    getline(file, s);
    getline(file, t);
    getline(file, t);

    tuple<string, string, int> edits = calculate_edits(s, t);

    cout << get<2>(edits) << '\n';
    cout << get<0>(edits) << '\n';
    cout << get<1>(edits) << '\n';
}

tuple<string, string, int> calculate_edits(string s, string t)
{
    pair<string, string> input = pair<string, string>(s, t);
    tuple<string, string, int> result;

    map<pair<string, string>, tuple<string, string, int>>::iterator itr = calculated_results.find(input);

    string s_suffix, s_prime, t_suffix, t_prime;
    int score;
    if (itr != calculated_results.end())
        return itr->second;
    else if (s.length() == 0 && t.length() == 0)
        result = make_tuple("", "", 0);
    else if (s.length() == 0)
    {
        s_prime = "";
        for (char c : t)
            s_prime.append("-");
        result = make_tuple(s_prime, t, t.length());
    }
    else if (t.length() == 0)
    {
        t_prime = "";
        for (char c : s)
            t_prime.append("-");
        result = make_tuple(s, t_prime, s.length());
    }
    else
    {

        s_suffix = s.substr(1, s.length() - 1);
        t_suffix = t.substr(1, t.length() - 1);

        if (s[0] == t[0])
        {
            result = calculate_edits(s_suffix, t_suffix);
            s_prime = s[0] + get<0>(result);
            t_prime = t[0] + get<1>(result);
            score = get<2>(result);
            result = make_tuple(s_prime, t_prime, score);
        }
        else
        {

            tuple<string, string, int> deletion = calculate_edits(s_suffix, t);
            tuple<string, string, int> insertion = calculate_edits(s, t_suffix);
            tuple<string, string, int> substitution = calculate_edits(s_suffix, t_suffix);

            int deletion_score = get<2>(deletion);
            int insertion_score = get<2>(insertion);
            int substitution_score = get<2>(substitution);
            if (deletion_score < insertion_score && deletion_score < substitution_score)
            {
                s_prime = s[0] + get<0>(deletion);
                t_prime = "-" + get<1>(deletion);
                score = 1 + deletion_score;
                result = make_tuple(s_prime, t_prime, score);
            }
            else if (insertion_score < deletion_score && insertion_score < substitution_score)
            {
                s_prime = "-" + get<0>(insertion);
                t_prime = t[0] + get<1>(insertion);
                score = 1 + insertion_score;
                result = make_tuple(s_prime, t_prime, score);
            }
            else
            {
                s_prime = s[0] + get<0>(substitution);
                t_prime = t[0] + get<1>(substitution);
                score = 1 + substitution_score;
                result = make_tuple(s_prime, t_prime, score);
            }
        }
    }

    calculated_results.insert(pair<pair<string, string>, tuple<string, string, int>>(input, result));
    return result;
}