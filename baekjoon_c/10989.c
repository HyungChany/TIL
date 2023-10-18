#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int c[10001] = { 0, };
    int x;
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        c[x] += 1;
    }

    for (int i = 1; i < 10001 ; i++) {
        if (c[i] > 0) {
            for (int j = 0; j < c[i]; j++) {
                printf("%d\n", i);
            }
        }
    }  
    return 0;
}