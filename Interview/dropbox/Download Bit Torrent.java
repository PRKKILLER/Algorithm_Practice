import java.io.*;
import java.util.*;

/*
* To execute Java, please define "static void main" on a class
* named Solution.
*
* If you need more classes, simply define them inline.
*/

    class Range {
    int lower;
    int higher;
    /* Implementation omitted */
    }

    // 0, 1,2,3,. ..7
    /* isFileDone([[3, 7), [0, 1), [2, 5), [6, 8)], 8) -> false */
    /* isFileDone([[3, 7), [0, 2), [2, 5), [6, 8)], 8) -> true */
    //blocks: [[0, 2), [2, 5), [3, 7),[6, 8)]

    class Solution {
        public boolean isFileDone(List<Range> blocks, int size) {
            Collections.sort(blocks, new Comparator<Range>() {
                @Override
                public compare(Range a, Range b) {
                    return a.lower-b.lower;
                }
            });
            Range pre = blocks.get(0);
            int i=1;
            while(i<blocks.size() && blocks.get(i).lower<=pre.higher) {
                pre.higher = Math.max(pre.higher,blocks.get(i).higher);
                i++;
            }
            if(pre.lower>0 || pre.higher<size) return false;
            return true;
        }
    }

    class Downloader {

        PriorityQueue<Range> pq;
        int size;

        public Downloader(int size) {
            // save size somewhere
            pq = new PriorityQueue(new Comparator<Range>() {
                @Override
                public compare(Range a, Range b) {
                    return a.lower-b.lower;
                }
            });
            this.size = size;
        }

        public void addBlock(Range r) {
            // TODO: implement
            pq.add(r);
            if(pq.size()>1) {
                Range pre = pq.poll();
                while(!pq.isEmpty() && pq.peek().lower<=pre.higher) {
                    pre.higher = Math.max(pre.higher, pq.poll().higher);
                }
                pq.add(pre);
            }
        }

        public boolean isDone() {
            // TODO: implement
            if(pq.isEmpty()) return false;
            Range minB = pq.peek();
            if(minB.lower>0 || minB.higher<size) return false;
            return true;
        }
}