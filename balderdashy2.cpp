//Balderdashy2

#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include <vector>

using namespace std;
//functions

struct Definition {

	string words;
	int player_number;
	bool correct;

};

void get_file_info(vector<string>* v, ifstream fin){



}

//main
int main() {

	int players;

	cout << "Welcome to Balderdashy2!\nPlease enter the number of players: ";
	cin >> players;
	assert(players > 0);

	cout << "\nWe will play with " << players << " players.\n";



	return 0;
}