#include <stdio.h>
int main(void) {
    int a[100001];
    long long b[100001];
    int n, m, i, j;
    long long c;
    scanf("%d %d", &n, &m);
 
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
        b[i] = b[i - 1] + a[i];
    }
 
    while (m--) {
        scanf("%d %d", &i, &j);
        c = b[j] - b[i - 1];
        printf("%lld\n", c);
    }
    return 0;
}