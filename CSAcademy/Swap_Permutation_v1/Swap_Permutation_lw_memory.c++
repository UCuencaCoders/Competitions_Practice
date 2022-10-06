#include <iostream>

using namespace std;

int p[100005];

int main() {
    int n,m,k;
    cin >> n >> m >> k;
    for (int i=1;i<=n;i++) p[i] = n+1;
    int pos = 1;
    for (int i=1;i<=m;i++){
        int x,y;
        cin >> x >> y;
        swap(p[x],p[y]);
        p[pos] = min(p[pos],i);
        if (pos == x || pos == y) pos = x + y - pos;

        for (int j=1;j<=n;j++) cout << p[j] << " ";
        cout << endl;

    }
    cout << p[k] << endl;
    system("pause");
}