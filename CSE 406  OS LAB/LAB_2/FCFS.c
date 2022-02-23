#include<stdio.h>

int main()
{
    int n;
    //total number of process
    scanf("%d",&n);
    int p[n];
    double avg;
    // burst time for each process
    for(int i=0;i<n;i++)
    {
       printf("For p%d: ", i+1);
       scanf("%d",&p[i]);
    }
    // chart
    printf("GANTT Chart:");
    int i=0, s=0, j=0, temp= n;
    while(temp--)
    {
        printf("%d p%d ",s,i);
        if(j<=n-1)
        {
            avg=avg+s;
        }
        s=s+p[i];
        i++;
        j++;
    }
    printf("%d\n",s);
    printf("Avg waiting time %.2f\n",avg/n);

return 0;
}
