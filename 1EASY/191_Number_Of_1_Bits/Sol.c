#include <stdio.h>
#include <stdint.h>
int hammingWeight(int n) {
    int count = 0;
    while (n > 0) {
        count += (n & 1); // 直接加 0 或 1，不用寫 if 更簡潔
        n >>= 1;
    }
    return count;
}

int main() {
    int nums[] = {11, 128, 2147483645};
    // 計算陣列大小 全長 / 單一元素長度
    int size = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < size; i++) {
        printf("Input: %d, Result: %d\n", nums[i], hammingWeight(nums[i]));
    }
    return 0;
}