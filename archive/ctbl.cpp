#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <vector>

using namespace std;

struct Node
{
    string name;
    Node *parent;
    vector<Node *> children;
};

Node *newNode();
Node *newNode(string name);
set<Node *> nontrivial_splits(Node *root);
void splitA(Node *root, Node *split, map<string, int> *characters);
void splitB(Node *split, map<string, int> *characters);

int main(void)
{
    string line;
    ifstream file("rosalind_ctbl.txt");

    getline(file, line);

    Node *root = newNode();

    Node *current = root;

    // Read the graph

    string name = ""; // name of the current node
    bool readingNeighbourName = false;
    bool readingCurrentName = false;
    Node *n;
    for (char c : line)
    {
        switch (c)
        {
        case '(':
            n = newNode();
            n->parent = current;
            current->children.push_back(n);
            current = n;
            readingNeighbourName = true;
            break;

        case ',':
            if (readingNeighbourName)
            {
                n = newNode(name);
                n->parent = current;
                current->children.push_back(n);
                name = "";
            }
            else if (readingCurrentName)
            {
                current->name = name;
                name = "";
                readingCurrentName = false;
                readingNeighbourName = true;
                current = current->parent;
            }
            break;

        case ')':
            if (readingNeighbourName)
            {
                n = newNode(name);
                n->parent = current;
                current->children.push_back(n);
                name = "";
                readingNeighbourName = false;
            }
            if (readingCurrentName)
                current = current->parent;
            readingCurrentName = true;
            break;

        case ';':
            if (readingCurrentName)
            {
                current->name = name;
                name = "";
                readingCurrentName = false;
            }
            break;

        default:
            name += c;
            break;
        }
    }

    // advance the root because the above
    // algorithm above adds one extra node
    root = root->children[0];
    root->parent = nullptr;

    // build partitions
    set<Node *> splits = nontrivial_splits(root);
    splits.erase(root);

    for (auto split : splits)
    {
        map<string, int> characters;
        splitA(root, split, &characters);
        splitB(split, &characters);
        for (auto x : characters)
            cout << x.second;
        cout << "\n";
    }
}

Node *newNode()
{
    Node *n = new Node();
    n->name = "";
    n->parent = nullptr;
    return n;
}

Node *newNode(string name)
{
    Node *n = newNode();
    n->name = name;
    return n;
}

// generates a set of nontrivial splits
set<Node *> nontrivial_splits(Node *root)
{
    set<Node *> splits;
    if (root->children.size() > 1)
        splits.insert(root);

    for (auto child : root->children)
        for (auto split : nontrivial_splits(child))
            splits.insert(split);

    return splits;
}

// calculates the first part of the split graph
void splitA(Node *root, Node *split, map<string, int>* characters)
{
    if (root == nullptr || root == split)
        return;

    if (root->children.empty())
        (*characters).insert(pair<string, int>(root->name, 0));
    for (auto child : root->children)
        splitA(child, split, characters);
}

// calculates the second part of the split graph
void splitB(Node *node, map<string, int>* characters)
{
    if (node == nullptr)
        return;
    if (node->children.empty())
        (*characters).insert(pair<string, int>(node->name, 1));
    for (auto child : node->children)
        splitB(child, characters);
}