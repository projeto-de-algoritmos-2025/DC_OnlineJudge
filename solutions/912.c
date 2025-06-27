#include <stdlib.h>

void merge(int* nums, int left, int mid, int right) {
    int size = right - left + 1;
    int* temp = (int*)malloc(size * sizeof(int));

    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j]) {
            temp[k++] = nums[i++];
        } else {
            temp[k++] = nums[j++];
        }
    }

    while (i <= mid) temp[k++] = nums[i++];
    while (j <= right) temp[k++] = nums[j++];

    for (i = left; i <= right; i++) {
        nums[i] = temp[i - left];
    }

    free(temp);
}

void mergeSort(int* nums, int left, int right) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;

    mergeSort(nums, left, mid);
    mergeSort(nums, mid + 1, right);
    merge(nums, left, mid, right);
}

int* sortArray(int* nums, int numsSize, int* returnSize){
    mergeSort(nums, 0, numsSize - 1);
    *returnSize = numsSize;
    return nums;
}
