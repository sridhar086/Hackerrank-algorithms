import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int[] revisedRussianRoulette(int[] doors) {
        // Complete this function
        int count = 0;
        for (int i = 0; i< doors.length; i++)
        {
            if( (i+1) != doors.length && (doors[i] == 1 && doors[i+1] == 1))
            {
                count +=1;
                i=i+1;             
            }
            else if (doors[i] == 1)
            {
                count +=1;                
            }
            else
            { }
        }
        int max_count = 0;
        for (int i = 0; i< doors.length;i++)
        {if (doors[i] ==1)
            max_count+=1;
        }
        int[] ar = {count , max_count};
        return ar;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] doors = new int[n];
        for(int doors_i = 0; doors_i < n; doors_i++){
            doors[doors_i] = in.nextInt();
        }
        int[] result = revisedRussianRoulette(doors);
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i != result.length - 1 ? " " : ""));
        }
        System.out.println("");
        in.close();
    }
}
