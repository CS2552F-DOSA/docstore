#include <cstdlib>
#include <fstream>
#include <sstream>

#include "chrono"
#include "iostream"
#include "string"
#include "time.h"

#pragma GCC target("avx2")
#pragma GCC optimization("O3")

// auto _ = []() {
//   std::ios::sync_with_stdio(false);
//   std::cin.sync_with_stdio(false);
//   std::cout.sync_with_stdio(false);
//   std::cin.tie(nullptr);
//   std::cout.tie(nullptr);
//   return 0;
// }();

int main(int argc, char** argv) {
  std::string dictionary;
  std::string target = "111\n444\n333";
  std::string delta;
  double count = 2000;

  // perpare data
  for (size_t i = 0; i < 3000; i++) {
    dictionary.append("111111111\n");
  }
  for (size_t i = 0; i < 3000; i++) {
    dictionary.append("222222222\n");
  }

  for (size_t i = 0; i < 4000; i++) {
    dictionary.append("444444444\n");
  }

  for (size_t i = 0; i < 2900; i++) {
    target.append("111111111\n");
  }
  for (size_t i = 0; i < 3100; i++) {
    target.append("222222222\n");
  }

  for (size_t i = 0; i < 4000; i++) {
    target.append("444444444\n");
  }

  //  std::cin >> count;

  std::ofstream outfile;
  std::ifstream infile;
  outfile.open("old", std::ios::out | std::ios::trunc);
  outfile << dictionary;
  outfile.close();
  outfile.open("new", std::ios::out | std::ios::trunc);
  outfile << target;
  outfile.close();
  size_t len;
  char ch;

  auto t1 = std::chrono::high_resolution_clock::now();
  auto t2 = std::chrono::high_resolution_clock::now();
  auto duration =
      std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1).count();
  for (int i = 0; i < count; i++) {
    t1 = std::chrono::high_resolution_clock::now();
    outfile.open("new", std::ios::out | std::ios::trunc);
    outfile << target;
    outfile.close();
    system("diff old new > delta");

    delta.clear();
    infile.open("delta", std::ios::in);

    std::stringstream ss;
    ss << infile.rdbuf();
    delta = ss.str();

    infile.close();

    outfile.open("delta", std::ios::out);
    outfile << delta;
    outfile.close();

    system("patch old delta > /dev/null 2>&1");

    outfile.open("old", std::ios::out | std::ios::trunc);
    outfile << dictionary;
    outfile.close();

    t2 = std::chrono::high_resolution_clock::now();
    duration +=
        std::chrono::duration_cast<std::chrono::seconds>(t2 - t1).count();
  }

  std::cout << "shell diff and patch time cost: " << duration / count
            << " second\n";

  return 0;
}