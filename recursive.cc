#include<iostream>

using namespace std;

class staircase
{
  int number; // Number of steps left
  int steps_at_a_time;
public:
  int total_steps = 0;
  int steps(int number, int steps_at_a_time)
  {
    if(number < 0)
      {
	return 0;
      }
    else if (number == 0)
      {
	return 1;
      }
    else
      {
	staircase one;
	for(int i=1; i <= steps_at_a_time; ++i)
	  {
	    total_steps = total_steps + one.steps(number-i, steps_at_a_time);
	  }
	//return one.steps(number-1,1)+one.steps(number-2,2);
      }
    return total_steps;
  };
};

// Recursive method for counting the number of possible ways
// of getting up some stairs using one or two steps


int main()
{
  int stairlength; int maximum_steps_at_a_time;
  cout << "Welcome to the stair running simulator. " << endl;
  cout << "Please enter the number of steps in the stairs: ";
  cin >> stairlength;
  cout << "Please enter the maximum number of steps the child is allowed to make at a time: ";
  cin >> maximum_steps_at_a_time;
  staircase running;
	  cout << "The child can run up the stairs in " << running.steps(stairlength,maximum_steps_at_a_time) << endl << " different way(s)." << endl;
  return 0;
}
