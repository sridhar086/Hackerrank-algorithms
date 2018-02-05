import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int h = in.nextInt();
        int m = in.nextInt();
        String[] numNames = {"","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen", "fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three",
                "twenty four",
                "twenty five",
                "twenty six",
                "twenty seven",
                "twenty eight",
                "twenty nine",        
    };
        int next=0;
        if(h==11)
            {next=1;}
        else{next=h+1;}
        
        if(m==0){System.out.println(numNames[h]+" o' clock");}
        else if(m==30){System.out.println("half past "+numNames[h]);}
        else if(m==15){System.out.println("quarter past "+numNames[h]);}
        else if(m==45){ System.out.println("quarter to "+numNames[next]);}
        else if (m<30){System.out.println(numNames[m]+" minutes past "+numNames[h]);}
        else{System.out.println(numNames[60-m]+" minutes to "+numNames[next]);}
}
}
