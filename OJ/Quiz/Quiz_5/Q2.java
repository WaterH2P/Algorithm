import java.util.*;

public class Main {
    static int max=-1;
    static int Num=0;
    public static void main (String[] args) {
        Scanner sc=new Scanner(System.in);
        int k=Integer.parseInt(sc.nextLine());
        for(;k>0;k--){
            prob(sc);
        }
    }
    private static void prob(Scanner sc) {
        int n=Integer.parseInt(sc.nextLine());
        String []tmp1=sc.nextLine().split(" ");
        String []tmp2=sc.nextLine().split(" ");

        int []ar=new int[n];
        int []le=new int[n];
        int [][]res=new int[24][60];

        for(int i=0;i<n;i++){
            ar[i]=Integer.parseInt(tmp1[i]);
            le[i]=Integer.parseInt(tmp2[i]);
        }
        for(int i=0;i<n;i++){
            int sn=ar[i]/100;
            int sm=ar[i]%100;

            int ln=le[i]/100;
            int lm=le[i]%100;

            for(int j=(sn-1)*60+sm,count=0;count<1+(ln-sn)*60+lm-sm;j++,count++){
                res[j/60][j%60]++;
            }
        }
        int max=0;
        for(int i=0;i<24;i++){
            for(int j=0;j<60;j++){
                max=Math.max(max,res[i][j]);
            }
        }
        System.out.println(max);
    }
}