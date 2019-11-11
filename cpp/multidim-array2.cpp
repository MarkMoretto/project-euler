
#include <iostream>
#include <numeric>
#include <vector>
#include "md-array.hxx"


int main(int argc, char ** argv) {

    // Using 5-day business week for brevity
    int temp[CITY][BUSWEEK];

    // Vectors to help compute average temperature of each city for the week.
    std::vector<double> vecCity1;
    std::vector<double> vecCity2;  

    // Initial salutation.
    std::cout << "Welcome to the WeatherMatrix!" << std::endl << "Please enter temperatures for city 1 and city 2 for the recent week:" << std::endl;

    for (int r = 0; r < CITY; ++r) {
        for (int c = 0; c <  BUSWEEK; ++c) {
            std::cout << "City " << r + 1 << " and Weekday " << c + 1 << " -> ";
            std::cin >> temp[r][c];
        }
    }

    std::cout << "The following results were recorded for the two cities:" << std::endl;

    for (int i = 0; i < CITY; ++i) {
        for (int j = 0; j < BUSWEEK; ++j) {
            std::cout << "City " << i + 1 << " and Weekday " << j + 1 << " = " << temp[i][j] << std::endl;

            // Determine if on city 1 or city 2; Push values to vectors accordingly.
            if (i == 0) {
                vecCity1.push_back(temp[i][j] * 1.0);
            } else {
                vecCity2.push_back(temp[i][j] * 1.0);
            }
        }
    }

    double avgTempCity1 = std::accumulate(vecCity1.begin(), vecCity1.end(), 0.0) / vecCity1.size();
    double avgTempCity2 = std::accumulate(vecCity2.begin(), vecCity2.end(), 0.0) / vecCity2.size();

    std::cout << "The average temperature for city 1 was: " << avgTempCity1 << std::endl;
    std::cout << "The average temperature for city 2 was: " << avgTempCity2 << std::endl;

    return 0;
}
