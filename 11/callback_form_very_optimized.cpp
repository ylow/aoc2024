#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <charconv>
bool even_digits(int64_t i, int64_t& divisor) {
  divisor = 10;
  if (i < 100) {
    return i >= 10;
  }
  while (i >= 100) {
    i = i / 100;
    divisor *= 10;
  }
  return i >= 10;
}

int64_t string_view_stoi(std::string_view sv) {
  int64_t i;
  std::from_chars(sv.data(), sv.data() + sv.size(), i);
  return i;
}
// Helper function to split a string
std::pair<int64_t, int64_t> splitNumber(int64_t stone, int64_t divisor) {
    int64_t left = stone / divisor;
    int64_t right = stone % divisor;
    return {left, right};
}

// Coroutine generator for stone_generator
template <typename F>
void StoneGenerator(int64_t stone, int64_t step, F f) {
    int64_t divisor;
    if (step == 0) {
        f(stone);
    } else if (stone == 0) {
        StoneGenerator(1, step - 1, f);
    } else if (even_digits(stone, divisor)) {
        auto [left, right] = splitNumber(stone, divisor);
        StoneGenerator(left, step - 1, f);
        StoneGenerator(right, step - 1, f);
    } else {
      StoneGenerator(stone * 2024, step - 1, f);
    }
}

// Coroutine generator for generate_all
template <typename F>
void GenerateAll(const std::vector<int64_t>& stoneList, int64_t step, F f) {
    for (int64_t stone : stoneList) {
      StoneGenerator(stone, step, f);
    }
}

int main() {
    std::vector<int64_t> stoneList = {  64599,31,674832,2659361,1,0,8867,321  };
    int64_t nsteps = 30;
    int64_t ctr = 0;

    GenerateAll(stoneList, nsteps, [&](int64_t) { ctr++; });

    std::cout << ctr << std::endl;

    return 0;
}
