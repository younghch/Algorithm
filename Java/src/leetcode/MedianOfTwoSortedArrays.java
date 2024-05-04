package leetcode;


public class MedianOfTwoSortedArrays {
//    public double findMedianSortedArrays(int[] numsA, int[] numsB) {
//        int countToFind = (numsA.length + numsB.length)/2;
//        int startIdxA = 0;
//        int endIdxA = numsA.length;
//        int startIdxB = 0;
//        int endIdxB = numsB.length;
//
//        while (startIdxA < endIdxA) {
//            int countA = (startIdxA+endIdxA)/2+1;
//            int countB = countNumberOfSmaller(numsB, numsA[countA-1], startIdxB, endIdxB);
//            int mergedCount = countA+countB;
//            if (mergedCount == countToFind){
//                // return
//            } else if (mergedCount < countToFind) {
//                startIdxA = countA-1;
//                startIdxB = countB-1;
//            } else {
//                endIdxA = countA;
//                endIdxB = countB;
//            }
//        }
//        if ((numsA.length+numsB.length)%2 == 0) {
//        }
//        else {
//
//        }
//    }
//
//    private int countNumberOfSmaller(int[] nums, int target, int startIdx, int endIdx) {
//        int idx = Arrays.binarySearch(nums, target, startIdx, endIdx);
//        if (idx > 0) return idx;
//        else return -idx;
//    }
}
