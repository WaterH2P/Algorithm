package Class4;

import java.util.Scanner;

public class p1 {

    public static void main(String[] args) {

        Scanner cin = new Scanner(System.in);
        int testcase = Integer.parseInt(cin.nextLine());

        while(testcase>0) {

            int num = Integer.parseInt(cin.nextLine());

            String[] s = cin.nextLine().split(" ");
            int[] arr = new int[num];
            for(int i = 0; i<num; i++){
                arr[i] = Integer.parseInt(s[i]);
            }

            System.out.println(maxSumSubarray(arr));





            testcase--;
        }
    }

    public static int maxSumSubarray(int[] a) {
        int n =a.length;

        int fi=0;
        int ma=a[0], su=a[0];

        int[] fw=new int[n];
        int[] bw=new int[n];

        fw[0]=a[0];
        for(int i=1; i<n; i++) {

            su=Math.max(a[i], (su+a[i]));
            ma=Math.max(ma, su);

            fw[i]=su;
        }

        su=ma=bw[n-1]=a[n-1];

        for(int i=n-2; i>=0; i--) {

            su=Math.max(a[i], (su+a[i]));
            ma=Math.max(ma, su);

            bw[i]=su;
        }

        int fans=ma;
        for(int i=1; i<(n-1); i++)
            fans=Math.max(fans, (fw[i-1]+bw[i+1]));

        return fans;
    }

}

