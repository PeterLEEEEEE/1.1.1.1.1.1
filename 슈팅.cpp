#include<iostream>
#include<Windows.h>
using namespace std;

void settings(){
	system("mode con cols=56 lines=30 | title ���ð���");
}

void gotoxy(int x, int y) {
	HANDLE consoleHandle = GetStdHandle(STD_OUTPUT_HANDLE);
	COORD pos;
	pos.X = x;
	pos.Y = y;
	SetConsoleCursorPosition(consoleHandle, pos);
}

void menu() {
	gotoxy(24 - 2, 2);
	cout << "> �� �� �� ��";
	gotoxy(24, 13);
	cout << "�� �� �� ��";
	gotoxy(24, 14);
	cout << "   �� ��   ";
	while (1) {
		int n = keyControl();
		
	}
}

int keyControl() {
	char temp = getch();

}


int main() {
	settings();
	menu();
	

	return 0;
}