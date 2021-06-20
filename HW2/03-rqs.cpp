#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

int count(0);
int SIZE(100);

double H(int n)
{
  double ans(0);

  for (int i = 1; i <= n; ++i)
    ans += 1.0/i;

  return ans;

}

template <class T>
int partition(vector<T> & A, int lo, int hi)
{
  int i(lo), j;

  for (j = lo; j < hi; ++j)
  {
    ++count;
    if (A[j] < A[hi])
      swap(A[i++], A[j]);
  }
  swap(A[i], A[hi]);
  return i;
}

template <class T>
void rqs (vector<T> & A, int lo, int hi)
{
  if (lo >= hi)
    return;

  swap(A[hi], A[lo + rand() % (hi-lo + 1)]);
  int k = partition(A, lo, hi);
  rqs(A, lo, k-1);
  rqs(A, k+1, hi);
}

void ex()
{
  int N(SIZE);
  vector<int> A(N);

  for (int i = 0; i < A.size(); ++i)
    A[i] = N-i;

  rqs(A, 0, N-1);

}  
 
int main()
{
  srand(time(0));

  int n;
  while (true)
  {

     cout << "Enter n: ";
     cin >> n;

     count = 0;
     for (int i = 1; i <= n; ++i)
       ex();

     cout << double(count)/ n << " vs " << 2*(SIZE+1)*H(SIZE) - 4*SIZE << endl;
  }
  return 0;
}
