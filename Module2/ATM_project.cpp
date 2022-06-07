
// My C++ implementation of a simple ATM machine

#include <iostream>
#include <stdlib.h>
#include <string>
#include <map>
using namespace std;


class Bank {

private:
	map<int, int> acct_nums;
	map<int, string> acct_names;
	map<int, int> acct_types;
	map<int, int> acct_bals;
	string name;
	int accnumber;
	int type;
	int amount = 0;
	int tot = 0;

public:
	// This function allows the user to create a new account
	void setvalue()
	{

		// Initializes random seed
		srand(time(NULL));

		while (1)
		{
			// Generates random account number between 100 and 999
			accnumber = rand() % 999 + 100;
			if (acct_nums.count(accnumber))
			{}
			else
			{
				acct_nums[accnumber] = accnumber;
				break;
			}
		}

		cout << "\n\nPlease enter your full name\n";
		cin.ignore();

		// gets the user's input information
		getline(cin, name);

		cout << "\nSelect account type:\n0. Checking\n1. Savings\n";
		cin >> type;

		cout << "\nEnter the amount of funds to be added:\n";
		cin >> tot;

		cout << "\nCongrats, your new account number is: " << accnumber << "\n";

		acct_names[accnumber] = name;
		acct_types[accnumber] = type;
		acct_bals[accnumber] = tot;
	}

	// Checks if account is valid
	bool check_info(int data)
	{
		if (acct_nums.count(data))
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	// Shows the user his/her balance and info
	void showdata()
	{
		int test;
		int hold;
		bool v1;

		while (1)
		{
			cout << "\n\nPlease enter your account number: ";
			cin >> test;
			v1 = check_info(test);
			hold = acct_types[test];
			if (v1)
			{
				cout << "\n\nName: " << acct_names[test] << endl;
				cout << "Account No: " << accnumber << endl;
				if (hold == 0)
				{
					cout << "Account type: " << "Checking" << endl;
				}
				else
				{
					cout << "Account type: " << "Savings" << endl;
				}
					cout << "Balance: " << acct_bals[test] << endl;
				break;
			}
			else
			{
				cout << "\n\nSorry, that account does not exist.\n";
			}
		}
	}

	// Allows for making deposits
	void deposit()
	{
		int a;
		int bal;
		bool v1;
		int test;
		cout << "\n\nPlease enter your account number: ";
		cin >> test;
		v1 = check_info(test);
		if (v1)
		{
			cout << "\n\nEnter amount to be Deposited\n";
			cin >> a;
			bal = acct_bals[test];
			acct_bals[test] = bal + a;
			cout << "New balance: " << acct_bals[test];
		}
	}

	// Allows for withdrawing funds
	void withdrawl()
	{
		int a;
		int bal;
		bool v1;
		int test;
		cout << "\n\nPlease enter your account number: ";
		cin >> test;
		v1 = check_info(test);
		if (v1)
		{
			cout << "\n\nEnter the withdraw amount\n";
			cin >> a;
			bal = acct_bals[test];
			acct_bals[test] = bal - a;
			cout << "New balance: " << acct_bals[test];
		}
	}
};

int main()
{
	Bank b;

	int choice;

	while (1) {
		cout << "\n\nPlease select one of the following options:\n";
		cout << "1. Create New Account\n";
		cout << "2. Balance Enquiry\n";
		cout << "3. Deposit Funds\n";
		cout << "4. Withdraw Funds\n";
		cout << "5. Cancel\n";
		cin >> choice;

		// Choices to select from
		switch (choice) {
		case 1:
			b.setvalue();
			break;
		case 2:
			b.showdata();
			break;
		case 3:
			b.deposit();
			break;
		case 4:
			b.withdrawl();
			break;
		case 5:
			exit(1);
			break;
		default:
			cout << "\nInvalid choice\n";
		}
	}
}
