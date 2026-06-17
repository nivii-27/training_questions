#include <stdio.h>

int main() {
    long long decimal;
    int binary[64];
    int i = 0;
    int count_ones = 0;

    if (scanf("%lld", &decimal) != 1) {
        printf("invalid input\n");
        return 0;
    }

    if (decimal <= 0) {
        printf("invalid input\n");
        return 0;
    }
    while (decimal > 0) {
        binary[i] = decimal % 2;
        if (binary[i] == 1) {
            count_ones++;
        }
        decimal = decimal / 2;
        i++;
    }
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
    printf("\n");
    if (count_ones > 0) {
        printf("%d\n", count_ones);
    } else {
        printf("invalid input\n");
    }

    return 0;
}
