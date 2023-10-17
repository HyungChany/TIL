#include<stdio.h>

int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);

	int arr[1000000];

	for (int i = 2; i <= b; i++) {
		arr[i] = 1;
	}

    for (int i = 2; i <= b; i++) {
        for (int j = i * 2; j <= b; j += i) {
            arr[j] = 0;
        }
    }

    for (int i = a; i <= b; i++) {
        if (arr[i] == 1) {
            printf("%d\n", i);
        }
    }

	return 0;
}