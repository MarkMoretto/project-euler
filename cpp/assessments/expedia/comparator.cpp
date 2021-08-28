
#include <iostream>
#include <vector>

using namespace std;

using IVEC = std::vector<int>;

    public:
    bool compare(int a, int b) {
        if (a == b) {
            return true;
        } else {
            return false;
        }
    }
    bool compare(string a, string b) {
        if (a == b) {
            return true;
        } else {
            return false;
        }
    }
    bool compare(IVEC a, IVEC b) {
        bool result = true;

        if (a.size() == b.size()) {

            for (int i = 0 i < a.size(); i++) {
                if (a[i] != b[i]) {
                    result = false;
                    break;
                }
            }
        } else {
            result = false;
        }
        return result;
    }
}

