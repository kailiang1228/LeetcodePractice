#include <stdio.h>
#include <stdint.h>

int reverseBits(int n) {
// 關鍵：將輸入轉為無號數，確保右移時左邊補 0 (邏輯右移)
    uint32_t un = (uint32_t)n; 
    uint32_t result = 0;

    for (int i = 0; i < 32; i++) {
        // 取得 un 的最右邊位元
        int bit = un & 1; 
        // 將 result 左移一位，並加上 bit
        result = (result << 1) | bit; 
        // 將 un 右移一位
        un >>= 1; 
    }

    // (int) 強制轉回有號整數
    return (int)result;
}

// 模擬測試
int main() {
    // 使用 uint32_t 陣列，這在處理暫存器資料時很常見
    uint32_t nums[] = {43261596, 2147483648};       //後者超過32位有號整數範圍
    // 計算陣列大小 全長 / 單一元素長度
    int size = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < size; i++) {
        // %u (無號十進位) 或 %u 搭配十六進位 %x
        printf("Input: %u, Result: %u\n", nums[i], reverseBits(nums[i]));
        printf("Input: %d, Result: %d\n", nums[i], reverseBits(nums[i]));
    }
    return 0;
}

// 964176192, 1073741822

// Bitwise 與 Signed：永遠不要對可能為負的 int 直接做 >>，除非你確定你想要的是算術右移
// 型別一致性：在處理底層暫存器或 LeetCode 位元題時，內部變數一律宣告為 uint32_t
// 通靈技巧：當結果出現一堆 1 或異常小的數字時，先檢查是不是「符號位元（Sign bit）」在搗亂