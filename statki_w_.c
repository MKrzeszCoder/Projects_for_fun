#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define N 10
#define M 10

int main(){
    int tablica[N][M];
    srand(time(NULL));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            tablica[i][j] = 0;
            
        }
    }

    int placed = 0;
    int x;
    int y;
    while (placed < 10) {
        x=rand()%M;
        y=rand()%N;
        if(tablica[y][x]==1)
            continue;
        tablica[y][x]=1;
        placed++;
    }

    int statki=10;
    int liczba,liczba2;
    printf("musisz ustrzelic 10 malych statkow, powodzenia!\n");
    while(statki>0){
        printf("Podaj jakie pole strzelasz kolumny a potem rzedy:");
        scanf("%d %d",&liczba,&liczba2);
        while(getchar()!='\n');
        if(tablica[liczba][liczba2]==1)
        {
            tablica[liczba][liczba2]=2;
            statki--;

            printf("Trafiles!\n");

        }
        if(tablica[liczba][liczba2]==0){
            tablica[liczba][liczba2]=3;
        }
        else if (tablica[liczba][liczba2] == 3) {
            printf("Oj w to pole juz strzelales!\n");
            continue;
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                 if (tablica[i][j] == 0 || tablica[i][j] == 1)
                    printf(" -");
                else if (tablica[i][j] == 2)
                    printf(" X");
                else
                    printf(" 0");
            }
            printf("\n");
        }

    }

printf("WOW wygrales gratulacje!\n");
    for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
               if (tablica[i][j] == 2)
                printf(" X");
            else
                printf(" -");
            }
            printf("\n");
        }
}
