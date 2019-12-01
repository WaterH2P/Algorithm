import java.util.*;

public class Main {
    static int max=-1;
    static int Num=0;
    public static void main (String[] args) {
        Scanner sc=new Scanner(System.in);
        int k=Integer.parseInt(sc.nextLine());

        for(;k>0;k--){
            max=-1;
            Num=0;
            prob(sc);
        }
    }
    private static void prob(Scanner sc) {
        int n=Integer.parseInt(sc.nextLine());
        int []pr=new int[n];
        int []dd=new int[n];
        String tmp[]=sc.nextLine().split(" ");
        for(int i=0;i<n;i++){
            dd[i]=Integer.parseInt(tmp[3*i+1]);
            pr[i]=Integer.parseInt(tmp[3*i+2]);
        }
        func(pr,dd,0,n,0,0,new ArrayList<>());
        System.out.println(Num+" "+max);
    }

    static void func(int[]pr,int[]dd,int time,int left,int profit,int num,List<Integer> indexs){
        for(int i=0;i<pr.length;i++){
            if(!indexs.contains(i)&&dd[i]==time){
                left--;
            }

        }
        if(left==0){
            if(max<profit){
                max=profit;
                Num=num;
            }

        }

        for(int i=0;i<pr.length;i++){
            if(dd[i]>time&&!indexs.contains(i)){
                indexs.add(i);
                func(pr,dd,time+1,left-1,profit+pr[i],num+1,indexs);
                indexs.remove(indexs.indexOf(i));
            }
        }

    }
}