/*         hevalino merheba min îro (16.2.2024) ji were li ser cpp'ê bi stêrkan qelp çêkir
                 hûn jî karin temaşe bikin û çekin xwe hîn bikin :)  
 */
#include<stdio.h>

int main()
{

int ref,sterk;

for (ref = 0; ref <= 2; ref++)
{
    for (sterk = 1; sterk <= 17; sterk++)
    {
        if ((sterk >= 3 - ref && sterk <= 6 + ref) || (sterk >= 12 - ref && sterk <= 15 + ref))
        
        printf("*"); //nîşankirina stêrkan

        else
        printf(" "); // valahî
    }
    printf("\n");
}

for (ref = 0; ref < 9 ; ref++)
{
    for (sterk = 1; sterk <= 17; sterk++)
    {
        if (sterk >= ref + 1 && sterk<= 17 - ref)
        printf("*");  // nîşankirina stêrkan 
        else
        printf(" "); //valahî
        
    }
    printf("\n");
}

printf("ha ji were qelpek xwesik. :) ");

return 0;
}