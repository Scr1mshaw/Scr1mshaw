#include <iostream>
#include <string>


using namespace std;

int main()
{
    char emptyspot1 = '1';
    char emptyspot2 = '2';
    char emptyspot3 = '3';
    char emptyspot4 = '4';
    char emptyspot5 = '5';
    char emptyspot6 = '6';
    char emptyspot7 = '7';
    char emptyspot8 = '8';
    char emptyspot9 = '9';




    int turn = 9;





    char board[3][3] =
    {
        {emptyspot1, emptyspot2, emptyspot3},
        {emptyspot4, emptyspot5, emptyspot6},
        {emptyspot7, emptyspot8, emptyspot9},
    };

    int playerone = 1, playertwo = 2;

    while (turn >= 0)

{

    int player = playerone;


    if (turn == 0)
    {
        cout << "Draw,nobody wins";
        break;
    }


    std::string chosensquare;

    cout << "choose a square, player " << player << endl;
    cin >> chosensquare;



if (player == 1)
{


    if (chosensquare == "1")
    {
        board[0][0] = 'x';
    }
    else if (chosensquare == "2")
    {
        board[0][1] = 'x';
    }
    else if (chosensquare == "3")
    {
        board[0][2] = 'x';
    }
    else if (chosensquare == "4")
    {
        board[1][0] = 'x';
    }
    else if (chosensquare == "5")
    {
        board[1][1] = 'x';
    }
    else if (chosensquare == "6")
    {
        board[1][2] = 'x';
    }
    else if (chosensquare == "7")
    {
        board[2][0] = 'x';
    }
    else if (chosensquare == "8")
    {
        board[2][1] = 'x';
    }
    else if (chosensquare == "9")
    {
        board[2][2] = 'x';
    }
}
else if (player == 2)
{


    if (chosensquare == "1")
    {
        board[0][0] = '0';
    }
    if (chosensquare == "2")
    {
        board[0][1] = '0';
    }
    if (chosensquare == "3")
    {
        board[0][2] = '0';
    }
    if (chosensquare == "4")
    {
        board[1][0] = '0';
    }
    if (chosensquare == "5")
    {
        board[1][1] = '0';
    }
    if (chosensquare == "6")
    {
        board[1][2] = '0';
    }
    if (chosensquare == "7")
    {
        board[2][0] = '0';
    }
    if (chosensquare == "8")
    {
        board[2][1] = '0';
    }
    if (chosensquare == "9")
    {
        board[2][2] = '0';
    }
}


    for (int y = 0; y < 3; y++)
    {
        if (y !=2 )
        {


        cout << endl;
        for (int x = 0; x < 3; x++)
        {
            if (x != 2)
            {
            cout << board[y][x];
            cout << "|" ;
            }
            else
            {
            cout << board[y][x]<<endl;
            }
        }
        cout << "-+-+-";
        }
        else
        {
                 cout << endl;
        for (int x = 0; x < 3; x++)
        {
            if (x != 2)
            {
            cout << board[y][x];
            cout << "|" ;
            }
            else
            {
            cout << board[y][x]<<endl;
            }
        }
        }

    }




    if ((board[0][0] == board[1][1]) && (board[1][1] == board[2][2]) )
    {
        cout << "player "  << player << " wins on 1,5,9";
        break;
    }
    if ((board[0][2] == board[1][1]) && (board[1][1] == board[2][0]) )
    {
        cout << "player "  << player << " wins on 3,5,7";
        break;
    }
    if ((board[0][0] == board[0][1]) && (board[0][0] == board[0][2]) )
    {
        cout << "player "  << player << " wins on 1,2,3";
        break;
    }
    if ((board[1][0] == board[1][1]) && (board[1][0] == board[1][2]) )
    {
        cout << "player "  << player << " wins on 4,5,6";
        break;
    }
    if ((board[2][0] == board[2][1]) && (board[2][0] == board[2][2]) )
    {
        cout << "player "  << player << " wins because 7,8,8";
        break;
    }
    if ((board[0][0] == board[1][0]) && (board[0][0] == board[2][0]) )
    {
        cout << "player "  << player << " wins on 1,4,7";
        break;
    }
    if ((board[0][1] == board[1][1]) && (board[0][1] == board[2][1]) )
    {
        cout << "player "  << player << " wins on 2,5,8";
        break;
    }
    if ((board[0][2] == board[1][2]) && (board[0][2] == board[2][2]) )
    {
        cout << "player " << player << " wins on 3,6,9";
        break;
    }
    turn --;
    std::swap(playerone,playertwo);
}
    return 0;
}
