int main() {
	int a;
	scanf("%d", &a);

	for (int i = a / 2; i < a; i++) {
		int c = i;
		int x = i;
		while (x > 0) {
			c += x % 10;
			x /= 10;
		}

		if (c == a) {
			printf("%d\n", i);
			break;
		}
		if (i == a - 1) {
			printf("0");
		}
	}
}