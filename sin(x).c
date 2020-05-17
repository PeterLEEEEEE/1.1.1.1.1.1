#include <stdio.h>
//짝수일 때 양수 홀수일 때 음수로 돌아가는 테일러 급수 

int factorial(int n)
{
	int fact=1;
	int x;
	for(x=1;x<=n;x++)
	{
		fact*=x;
	}
	return fact;
}

double power(double x, int n)
{
	int i;
	double pow=1;
	for(i=1;i<=n;i++)
	{
		pow*=x;
	}
	return pow;
}


double sin(double x, double precision){
double sum = 0.0;

	for(int i=0; ;i++)
	{
		 double t = power(-1,i)*power(x,2*i+1)/factorial(2*i+1);
		if ((t<0 && -t<precision) || (t>=0 && t<precision)) break;
		sum = sum + t;
	}
	return sum;
}

int main() {
	float x, precision;
	scanf("%f %f", &x, &precision);
	printf("%.4f", sin(x, precision));
	
	return 0;
}
