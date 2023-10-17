#include<stdio.h>

int main(void) {
	int a,c;
	scanf("%d", &a);
	if (a < 100) {
		printf("%d", a);
	}
	else {
		c = 0;
		for (int i = 111; i <= a; i++) {
			int q, w, e;
			q = i % 10;
			w = (i / 10) % 10;
			e = (i / 10) / 10;
			if (q - w == w - e) {
				c++;
			}
		}
		printf("%d", 99 + c);
	}
	return 0;
}