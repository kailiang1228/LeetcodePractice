#include <stdio.h>
#include <stdint.h>

int singleNumber(int* nums, int numsSize) {
    int result = 0;
    for (int i = 0; i < numsSize; i++) {
        // XOR 運算 (相同為0，不同為1)
        result ^= nums[i];
    }
    return result;
}

// 模擬測試
int main() {
    int case1[] = {2, 2, 1};
    int size1 = sizeof(case1) / sizeof(case1[0]);
    
    int case2[] = {4, 1, 2, 1, 2};
    int size2 = sizeof(case2) / sizeof(case2[0]);

    int case3[] = {1};
    int size3 = sizeof(case3) / sizeof(case3[0]);

    // 執行測試並列印結果
    printf("Test 1 Result: %d (Expected: 1)\n", singleNumber(case1, size1));
    printf("Test 2 Result: %d (Expected: 4)\n", singleNumber(case2, size2));
    printf("Test 3 Result: %d (Expected: 1)\n", singleNumber(case3, size3));

    return 0;
}

// 1, 4, 1
