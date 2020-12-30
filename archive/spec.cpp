#include <iostream>
#include <cmath>
#include <fstream>
#include <iterator>
#include <map>

using namespace std;

char AA_from_mass(float mass, map<float, char> mass_table);

int main()
{

    // monoisotopic mass table
    map<float, char> mass_table;

    mass_table.insert(pair<float, char>(57.02146, 'G'));
    mass_table.insert(pair<float, char>(71.03711, 'A'));
    mass_table.insert(pair<float, char>(87.03203, 'S'));
    mass_table.insert(pair<float, char>(97.05276, 'P'));
    mass_table.insert(pair<float, char>(99.06841, 'V'));
    mass_table.insert(pair<float, char>(101.04768, 'T'));
    mass_table.insert(pair<float, char>(103.00919, 'C'));
    mass_table.insert(pair<float, char>(113.08406, 'I'));
    mass_table.insert(pair<float, char>(114.04293, 'N'));
    mass_table.insert(pair<float, char>(115.02694, 'D'));
    mass_table.insert(pair<float, char>(128.05858, 'Q'));
    mass_table.insert(pair<float, char>(128.09496, 'K'));
    mass_table.insert(pair<float, char>(129.04259, 'E'));
    mass_table.insert(pair<float, char>(131.04049, 'M'));
    mass_table.insert(pair<float, char>(137.05891, 'H'));
    mass_table.insert(pair<float, char>(147.06841, 'F'));
    mass_table.insert(pair<float, char>(156.10111, 'R'));
    mass_table.insert(pair<float, char>(163.06333, 'Y'));
    mass_table.insert(pair<float, char>(186.07931, 'W'));
    // mass_table.insert(pair<char, float>(113.08406, 'L'));
    
    string line;    
    ifstream file("rosalind_spec.txt");

    getline(file,line);
    float previous = stof(line);
    float current;
    while (getline(file, line))
    {
        current = stof(line);
        char AA = AA_from_mass(current-previous, mass_table);
        previous = current;
        cout << AA;
    }

    // Close the file
    file.close();
}

char AA_from_mass(float mass, map<float, char> mass_table) {

    map<float, char>::iterator itr; 
    
    for (itr = mass_table.begin(); itr != mass_table.end(); ++itr) { 
        if (abs(itr->first - mass) < 0.01)
        {
            return itr->second;
        }
    } 

    return ' ';
}