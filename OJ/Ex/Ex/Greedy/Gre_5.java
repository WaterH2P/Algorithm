public class Gre_5 {

    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        int t = Integer.parseInt(cin.nextLine());

        while(t-->0){
            String[] s = cin.nextLine().split(" ");
            int N = Integer.parseInt(s[0]);
            int M = Integer.parseInt(s[1]);

            int[] num1 = new int[N];
            int[] num2 = new int[M];

            String[] s1 = cin.nextLine().split(" ");
            String[] s2 = cin.nextLine().split(" ");

            for(int i=0;i<N;i++){
                num1[i]=Integer.parseInt(s1[i]);
            }
            for(int i=0;i<M;i++){
                num2[i]=Integer.parseInt(s2[i]);
            }

            int i=0;
            int j=0;
            int first=0;
            int second =0;
            int res=0;

            while(i<N&&j<M){
                if(num1[i]<num2[j]){first=first+num1[i]; i++;}
                else if(num1[i]>num2[j]){second=second+num2[j]; j++;}
                else{
                    res=res+Math.max(first,second)+num1[i];
                    first=0;
                    second=0;
                    i++;
                    j++;
                }
            }

            while (i < N) {
                res=res+num1[i]; i++;
            }
            while (j < M) {
                res=res+num2[j]; j++;
            }

            System.out.println(res);
        }
    }
}