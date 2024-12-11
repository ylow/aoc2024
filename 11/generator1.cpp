#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <coroutine>
#include "generator.h"

// Helper function to split a string
std::pair<int64_t, int64_t> splitNumber(int64_t stone) {
    std::string z = std::to_string(stone);
    int64_t k = z.size() / 2;
    int64_t left = std::stoi(z.substr(0, k));
    int64_t right = std::stoi(z.substr(k));
    return {left, right};
}

// Coroutine generator for stone_generator
std::generator<int64_t> StoneGenerator(int64_t stone, int64_t step) {
    if (step == 0) {
        co_yield stone;
    } else if (stone == 0) {
        for (int64_t value : StoneGenerator(1, step - 1)) {
            co_yield value;
        }
    } else if (std::to_string(stone).size() % 2 == 0) {
        auto [left, right] = splitNumber(stone);
        for (int64_t value : StoneGenerator(left, step - 1)) {
            co_yield value;
        }
        for (int64_t value : StoneGenerator(right, step - 1)) {
            co_yield value;
        }
    } else {
        for (int64_t value : StoneGenerator(stone * 2024, step - 1)) {
            co_yield value;
        }
    }
}

// Coroutine generator for generate_all
std::generator<int64_t> GenerateAll(const std::vector<int64_t>& stoneList, int64_t step) {
    for (int64_t stone : stoneList) {
        for (int64_t value : StoneGenerator(stone, step)) {
            co_yield value;
        }
    }
}

int main() {
    std::vector<int64_t> stoneList = {  64599,31,674832,2659361,1,0,8867,321  };
    int64_t nsteps = 30;
    int64_t ctr = 0;

    for (int64_t value : GenerateAll(stoneList, nsteps)) {
        ++ctr;
    }

    std::cout << ctr << std::endl;

    return 0;
}
