#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;

int count = 0;

struct TrieNode
{
    int ID;
    bool isLeaf;
    unordered_map<char, TrieNode *> map;
};

TrieNode *getNewTrieNode();
bool insert(TrieNode *root, string s);
void printTrie(TrieNode *root);

int main(void)
{
    string line;
    ifstream file("rosalind_trie.txt");

    TrieNode *root = getNewTrieNode();

    while (getline(file, line))
        insert(root, line);

    printTrie(root);
}

TrieNode *getNewTrieNode()
{
    TrieNode *node = new TrieNode;
    count++;
    node->ID = count;
    node->isLeaf = false;

    return node;
}

bool insert(TrieNode *root, string s)
{
    TrieNode *current = root;
    char c;
    int n = s.length();
    for (int i = 0; i < n; i++)
    {
        c = s[i];
        unordered_map<char, TrieNode *>::iterator itr = current->map.find(c);
        if (itr != current->map.end())
            current = itr->second;
        else
        {
            current->map.insert(pair<char, TrieNode *>(c, getNewTrieNode()));
            current = current->map.find(c)->second;
        }
        
        if (i == n-1) {
            current->isLeaf = true;
        }
    }

    return true;
}

void printTrie(TrieNode *root)
{
    for (auto it = root->map.begin(); it != root->map.end(); ++it)
    {
        cout << root->ID << " " << it->second->ID << " " << it->first << "\n";
        printTrie(it->second);
    }
}