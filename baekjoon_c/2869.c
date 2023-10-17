#include<stdio.h>

int main(void) {
	int a, b, x;
	scanf("%d %d %d", &a, &b, &x);
	if (a == x) {
		printf("%d", 1);
	}
	else if ((x - a) < (a - b)) {
		printf("%d", 2);
	}
	else if ((x - a) % (a - b) == 0) {
		printf("%d", (x - a) / (a - b) + 1);
	}
	else {
		printf("%d", (x - a) / (a - b) + 2);
	}
	return 0;
}