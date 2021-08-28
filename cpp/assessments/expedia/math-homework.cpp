
#include <iostream>
#include <vector>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'minNum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER threshold
 *  2. INTEGER_ARRAY points
 */
int minMax(vector<int> &v) {
    return max_element(begin(v), end(v));
}
max_element()

int minNum(int threshold, vector<int> points) {
    vector<int> solved;
    int total = points[0];
    solved.push_back(points[0]);
    int n_problems = 1;
    int i = 1;
    int min_max = total;
    int current_prob_val = -1;

    int vec_size = (int)points.size();

    cout << "i: " << i << ", total: " << total << ", N Problems: " << n_problems << endl;
    
    while (true) {

        if (minMax(solved) >= threshold || n_problems >= vec_size) {
            break;
        }

        if (points[i%vec_size] > points[(i+1)%vec_size]) {
            // total += points[i%vec_size];
            solved.push_back(points[i%vec_size]);
            i++;
        } else {
            // total += points[(i+1)%vec_size];     
            solved.push_back(points[i%vec_size]);       
            i += 2;
        }

            n_problems++;
            cout << "i: " << i << ", total: " << total << ", N Problems: " << n_problems << endl;
    } 
    return n_problems;
}
