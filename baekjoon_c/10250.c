#include<stdio.h>

int main(void) {
	int t,y,x,a;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d %d %d", &y, &x, &a);

		if (a % y == 0) {
			printf("%d%02d\n",  y,a / y);
		}
		else {
			printf("%d%02d\n", a%y,a/y+1);
		}
	}
	return 0;
}
