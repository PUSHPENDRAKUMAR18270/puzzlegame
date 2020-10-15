#include<iostream>
#include<string.h>
#include <bits/stdc++.h>
#include <ctime>
#define ll long long int
using namespace std;
int overs=2;
enum teamorder{first=1,second};
teamorder ord=first;
class match;
struct player
{
   int runs_scored;
   int balls_faced;
   int boundaries_scored;
   int wickets_taken;
};
struct scorecard{
  int runs;
   int overs;
   int balls;
   int boundaries;
   int wickets;
};

class team{
  
    player players[12];
        scorecard team_scorecard;
    public:  
    team(){team_scorecard={0,0,0,0,0};/*players[12]={{0,0,0,0},{0,0,0,0},{0,0,0,0},
    {0,0,0,0},{0,0,0,0},{0,0,0,0}
    ,{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};*/
        for(int i=0;i<12;i++)
        {
            players[i].runs_scored=0;
            players[i].balls_faced=0;
            players[i].boundaries_scored=0;
            players[i].wickets_taken=0;
        }
    } 
    void generate_player_score(player &p);
    void generate_team_scorecard();
    friend void playmatch(team inn,match m);
};
void team::generate_player_score(player &p)
{
  cout<<"PLAYER SCORE"<<endl;
    cout<<p.runs_scored<<"("<<p. balls_faced<<")"<<"("<<p.boundaries_scored<<")"<<endl;
}
void team::generate_team_scorecard(){
    cout<<"TEAM SCORECARD\n";
   cout<<team_scorecard.runs<<"("<<team_scorecard.overs<<"."<<team_scorecard.balls%6<<")"<<"("<<team_scorecard.boundaries<<")"<<"("<<team_scorecard.wickets<<")"<<endl;
}
class match:public team
{
  int currentplayer1,currentplayer2;
  int counter;
    public:
      match(){currentplayer1=1;currentplayer2=2;counter=2;}
      friend void playmatch(team inn,match m);

};
void playmatch(team inn,match m)
{
    
    for(int j=0;j<overs;j++)
    {
      int t,w,flag=0,count=0;
      if(inn.team_scorecard.wickets==11)
         break;
     for(int i=0;i<6;i++)
     {
         if(inn.team_scorecard.wickets==11)
        break;
         //srand(time(NULL));
         t=rand()%7;
           w=rand()%10;
           if(w==7)
           {
             if(flag==0)
             {
              inn.players[m.currentplayer1].balls_faced++;
              inn.generate_player_score(inn.players[m.currentplayer1]);
              m.currentplayer1=++m.counter;
             }
             else {
              inn.generate_player_score(inn.players[m.currentplayer2]);
              m.currentplayer2=++m.counter;
             }
             inn.team_scorecard.wickets++;
             inn.team_scorecard.balls++;
             continue;
           }
           
              //count++;
              int exchange_turns=0;
           if(exchange_turns==0)
           {
            inn.players[m.currentplayer1].runs_scored+=t;
             inn.team_scorecard.runs+= t;
            inn.players[m.currentplayer1].balls_faced++;
             if(t==4||t==6)
             {
                inn.players[m.currentplayer1].boundaries_scored++;
                  inn.team_scorecard.boundaries++;
                //inn.players[m.currentplayer1].balls_faced++; 
             }
             //flag=0;
             if(t%2!=0)
             exchange_turns=1;
           }
           else
           {
             inn.players[m.currentplayer2].runs_scored+=t;
              inn.team_scorecard.runs+= t;
               inn.players[m.currentplayer2].balls_faced++;
             if(t==4||t==6)
            { 
              inn.players[m.currentplayer2].boundaries_scored++;
              inn.team_scorecard.boundaries++;
             
            }
            //flag=1;
            if(t%2!=0)
            exchange_turns=0;
           }
           inn.team_scorecard.balls++;
           
     }
     
      inn.team_scorecard.overs++;
    }
    cout<<"the score cards of the current players are\n";
    inn.generate_player_score(inn.players[m.currentplayer1]);
     inn.generate_player_score(inn.players[m.currentplayer2]);
    cout<<"the team has finished batting and the final score for team "<<ord<<"is"<<endl;
    ord=second;
    
   inn.generate_team_scorecard();
}
int main()
{
match inning1;
team team1;
srand(time(NULL));
playmatch(team1,inning1);
match inning2;
team team2;
playmatch(team2,inning2);
}