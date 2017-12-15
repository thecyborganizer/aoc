#include <stdio.h>
#include <vector>
#include <cstdint>
#include <queue>

uint64_t generate(uint64_t value, uint64_t factor) {
    return (value * factor) % 2147483647;
}

bool compare(int a, int b) {
    return (a & 0xFFFF) == (b & 0xFFFF);
}


int main() {
    using namespace std;
    //uint64_t a = 65;
    //uint64_t b = 8921;
    uint64_t a = 289;
    uint64_t b = 629;
    queue<uint64_t> alist;
    queue<uint64_t> blist;
    int count = 0;
    int comparisons = 0;
    while (comparisons < 5000000) {
        if (comparisons % 100000 == 0) {
            printf("%d\n", comparisons);
        }
        a = generate(a, 16807);
        b = generate(b, 48271);
        if (a % 4 == 0) {
            alist.push(a);
        }
        if (b % 8 == 0) {
            blist.push(b);
        }
        while (!alist.empty() && !blist.empty()) {
            comparisons += 1;
            if (compare(alist.front(), blist.front())) {
                count += 1;
            }
            alist.pop();
            blist.pop();
        }
    }

    printf("%d\n", count);
}



