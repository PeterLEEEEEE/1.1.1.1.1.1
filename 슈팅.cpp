#include<iostream>
#include<Windows.h>
using namespace std;

void settings(){
	system("mode con cols=56 lines=30 | title 슈팅게임");
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
	cout << "> 게 임 시 작";
	gotoxy(24, 13);
	cout << "게 임 정 보";
	gotoxy(24, 14);
	cout << "   종 료   ";
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