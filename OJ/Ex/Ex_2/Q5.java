

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner cin = new Scanner(System.in);
        while(cin.hasNext()){
            String s =cin.nextLine();

            String[] nums = s.split(" ");
            int[] arr = new int[Integer.parseInt(nums[0])];
            for(int i=0;i<Integer.parseInt(nums[0]);i++){
                arr[i]=Integer.parseInt(nums[i+1]);
            }
            int[] result = bubbleSort(arr);
            System.out.print(result[0]);
            for(int i=1;i<result.length;i++){
                System.out.print(" "+result[i]);
            }
            System.out.println();

        }

    }

    public static int[] bubbleSort(int[] arr){

        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length-1;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
        return arr;
    }
}

