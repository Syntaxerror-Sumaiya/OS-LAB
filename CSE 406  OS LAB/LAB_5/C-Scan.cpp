#include <bits/stdc++.h>
using namespace std;

int size ;
int disk_size = 200;

void CSCAN(int arr[], int head)
{
    int headposition=head;
    int seek_count = 0;
    int distance, cur_track;
    vector<int> left, right;
    vector<int> seek_sequence;

    left.push_back(0);
    right.push_back(disk_size - 1);


    for (int i = 0; i < size; i++)
    {
        if (arr[i] < head)
            left.push_back(arr[i]);
        if (arr[i] > head)
            right.push_back(arr[i]);
    }

    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    for (int i = 0; i < right.size(); i++)
    {
        cur_track = right[i];
        seek_sequence.push_back(cur_track);

        distance = abs(cur_track - head);
        if(head>cur_track)
        {
            printf("(%d - %d)",head,cur_track);

        }
        else
            printf("(%d - %d)",cur_track,head);

        seek_count += distance;

        head = cur_track;
    }

    head = 0;

    seek_count += (disk_size - 1);

    for (int i = 0; i < left.size(); i++)
    {
        cur_track = left[i];

        seek_sequence.push_back(cur_track);

        distance = abs(cur_track - head);
        if(head>cur_track)
        {
            printf("(%d - %d)",head,cur_track);

        }
        else
            printf("(%d - %d)",cur_track,head);

        seek_count += distance;

        head = cur_track;
    }
    cout<<"\n";
    cout << "Total number of seek operations = "
         << seek_count << endl;

    cout << "Seek Sequence is: " ;
    cout<<headposition<<" ";
    for (int i = 0; i < seek_sequence.size(); i++)
    {
        cout << seek_sequence[i] << " ";
    }
}


int main()
{


    int arr[20] ;
    int head ;
    printf("Enter the number of Requests\n");
    scanf("%d",&size);
    printf("Enter the Requests sequence\n");
    for(int i=0;i<size;i++)
     scanf("%d",&arr[i]);
    printf("Enter initial head position\n");
    scanf("%d",&head);


    cout << "Initial position of head: " << head << endl;
    CSCAN(arr, head);

    return 0;
}
