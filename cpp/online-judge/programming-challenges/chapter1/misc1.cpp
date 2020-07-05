
/**
 * Random stackoverflow:
 * https://stackoverflow.com/questions/62736012/optimization-problems-in-c
*/

#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;


// vector<int>recorrido;
// vector<int>base;

vector<int> split_input(string inputs, string delim = " ") {
    vector<string> tmps;
    vector<int> outv;

    auto start = 0U;
    auto end = inputs.find(delim);
    while (end != string::npos) {
        tmps.push_back(inputs.substr(start, end - start));
        start = end + delim.length();
        end = inputs.find(delim, start);
    }
    tmps.push_back(inputs.substr(start, end));

    // Convert to integer.
    stringstream ss;
    int ii;
    for (auto &c : tmps) {
        ss << c;
        ss >> ii;
        outv.push_back(ii);
    }
    return outv;
}

// int suma_elementos(int elemento);
void suma_elementos(int elemento, int & consec, int proporcion);

int main() {

    int a_size, b_cons, final = 9999999, total = 0;
    int consecutivo;
    int proporcion;

    vector<int> recorrido, base;
    vector<int> dimv, arrv, consv;

    // Strings to hold user input values.
    string dims, arrange, consec;

    cout << "Welcome to the Program!" << endl << endl;
    cout << "When prompted, please enter all values with a single space inbetween them." << endl << endl;

    cout << "Enter array size and number of consecutive values: " << endl;
    getline(cin, dims);
    arrv = split_input(dims);
    a_size = arrv[0];
    b_cons = arrv[1];

    // cin >> a >> b;

    cout << "Enter " << a_size << " integer values: " << endl;
    getline(cin, arrange);
    arrv = split_input(arrange);

    for (auto &valor : arrv) {
        recorrido.push_back(valor);
    }

    cout << "Enter " << b_cons << " consecutive integer values: " << endl;
    getline(cin, consec);
    consv = split_input(consec);    

    for (auto &valor : consv) {
        base.push_back(valor);
    }

    // for (int i = 0; i < a; i++) {
    //     cin >> valor;
    //     recorrido.push_back(valor);
    // }

    // for (int i = 0; i < b; i++) {
    //     cin >> valor;
    //     base.push_back(valor);
    // }

    for (int i = 0; i < b; i++) {
        int v_sz=recorrido.size();

        suma_elementos(base[i], consecutivo, v_sz);

        for (int j = 0; j < consecutivo; j++) {
            for (int c = 0; c < base[i]; c++) {
                total += recorrido[c + (j)];
            }

            if (total < final) {
                final = total;
            }
            total = 0;
        }
        cout << final << " ";
        //reset
        consecutivo = 0;
        final = 99999999;
        total = 0;
    }

    return 0;
}

//Suma de elementos
void suma_elementos(int elemento, int & consec, int proporcion) {

    while (proporcion >= elemento) {
        proporcion--;
        consec++;
    }
    //cout << consecutivo << " ";
    // return 0;
}

// //Suma de elementos
// int suma_elementos(int elemento, int proporcion){

//     while (proporcion >= elemento) {
//         proporcion--;
//         consecutivo++;
//     }
//     //cout << consecutivo << " ";
//     return 0;
// }




// vector<int> split_input(string inputs, string delim = " ") {
//     std::size_t last = 0;
//     std::size_t next = 0;
//     string tmp;
//     char* tmpc = &tmp;
//     vector<string> tempv;

//     vector<int> out;
//     out.reserve(15);
    
//     while ((next = inputs.find(delim, last)) != string::npos) {
//         tmp = inputs.substr(last, next-last);
//         tmpc = tmp;
//         tempv.push_back(tmp);
//         last = next + 1;
//     }

//     tmp = inputs.substr(last);
//     tempv.push_back(tmp);
//     for (string &c : tempv) {
//         out.push_back(atoi(&c));

//     }
// }