import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();
        for (int i = 1; i <= t; ++i) {

            int n = in.nextInt();
            int k = in.nextInt();

            StringBuilder sb = new StringBuilder();
            for (int o = k; o > 0; o--) {
                sb.append(o == 1 ? o : o + " ");
            }

            StringBuilder array = new StringBuilder();
            for (int c = 0; c < n; c++) {
                array.append(c == n - 1 ? in.nextInt() : in.nextInt() + " ");
            }

            int count = 0;
            for (int a = 0; a < array.length(); a++) {
                int index = array.substring(a).indexOf(sb.toString());
                a += index;
                if (index == -1)
                    a = array.length();
                else
                    count++;
            }

            System.out.println("Case #" + i + ": " + count);
        }
    }
}