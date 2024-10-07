#include <stdio.h>
#include <math.h>
#define NUM 2
#define NN 20
#define cnum 2

typedef struct {
    double x[NUM];
}PATTERN;

PATTERN p[NN]={
    {0,0},{1,0},{0,1},{1,1},{2,1},{1,2},{2,2},{3,2},{6,6},{7,6},
    {8,6},{6,7},{7,7},{8,7},{9,7},{7,8},{8,8},{9,8},{8,9},{9,9}
};

PATTERN z[cnum],oldz[cnum];
int nj[cnum];
int cindex[cnum][NN];
double Eucliden(PATTERN x, PATTERN y)
{
    int i;
    double d;
    d=0.0;
    for(i=0;i<NUM;i++){
        d+=(x.x[i]-y.x[i])*(x.x[i]-y.x[i]);

    }
    d=sqrt(d);
    return d;

}

bool zequal( PATTERN z1[] , PATTERN z2[] )
{
    int j;
    double d;
    d=0.0;
    for(j=0;j<cnum;j++){
        d+=Eucliden(z1[j],z2[j]);
    }
    if(d<0.00001)return true;
    else return false;

}

void C_mean()
{
    int i,j,l;
    double d,dmin;
    for(j=0;j<cnum;j++){
        z[j]=p[j];
    }
    do{
        for(j=0;j<cnum;j++){
            nj[j]=0;
            oldz[j]=z[j];

        }
        for(i=0;i<NN;i++){
            for(j=0;j<cnum;j++){
                d=Eucliden(z[j],p[i]);
                if(j==0){dmin=d;l=0;}
                else{
                    if(d<dmin){
                        dmin=d;
                        l=j;

                    }
                }
            }
            cindex[l][nj[l]]=i;
            nj[l]++;
        }
        for(j=0;j<cnum;j++){
            if(nj[j]==0) continue;
            for(i=0;i<NUM;i++){
                d=0.0;
                for(l=0;l<nj[j];l++){
                    d+=p[cindex[j][l]].x[i];
                }
                d/=nj[j];
                z[j].x[i]=d;
            }
        }
    }while(!zequal(z,oldz));
}

void Out_Result()
{
    int i,j;
    printf("Result:\n");
    for(j=0;j<cnum;j++){
        printf("nj[%d]=%d\n",j,nj[j]);
        for(i=0;i<nj[j];i++){
            printf("%d,",cindex[j][i]);
        }
        printf("\n");
    }
}

int main(int argc,char * argv[])
{
    C_mean();
    Out_Result();
    return 0;
}

