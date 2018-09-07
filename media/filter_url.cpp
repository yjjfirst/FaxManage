#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>

using namespace std;

char in_str[1111], tmp_str[1111], res[1111];

int main() {
	freopen("temp.txt", "r", stdin);
	freopen("result.txt", "w", stdout);
	while (gets(in_str) > 0) {
		strlwr(in_str);
		memset(tmp_str, 0, sizeof(tmp_str));
		memset(res, 0, sizeof(res));
		int pos1 = strstr(in_str, "@github") - in_str;
		if (pos1 < 0) {
			continue;
		}
		strcat(tmp_str, in_str + pos1);
		int pos2 = strchr(tmp_str, '"') - tmp_str;
		strncpy(res, tmp_str + 1, pos2 - 1);
		printf("https://%s/archive/master.zip\n", res);
	}
	return 0;
}
