#include <stdio.h>

int main() {
	int a;
	scanf_s("%d", &a);
	int x = 1;
	int c = 1;
	while (a>0) {
		if (a <= x) {
			printf("%d\n", c);
			break;
		}
		else {
			x += 6 * c;
			c++;
		}
	}
}