#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    long long int arr[101] = { 0,1,1,1,2,2,3 };
    for (int i = 7; i < 101; i++) {
            arr[i] = arr[i - 1] + arr[i - 5];
    }
    for (int i = 0; i < t; i++) {
        int a;
        scanf("%d", &a);

        printf("%lld\n", arr[a]);
    }

    return 0;
}