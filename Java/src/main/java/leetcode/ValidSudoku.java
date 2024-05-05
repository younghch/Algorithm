package leetcode;

// https://leetcode.com/problems/valid-sudoku
public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            if (!validateRow(board, i) || !validateColumn(board, i)) return false;
        }
        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < board.length; j += 3) {
                if (!validateSquare(board, i, j)) return false;
            }
        }
        return true;
    }

    boolean validateRow(char[][] board, int rowIdx) {
        char[] row = board[rowIdx];
        int checkBit = 0;
        for (int i = 0; i < row.length; i++) {
            char num = row[i];
            if (num == '.') continue;
            int toCheckBit = (int) Math.pow(2, num-'0');
            if ((checkBit & toCheckBit) != 0) return false;
            checkBit = checkBit | toCheckBit;
        }
        return true;
    }

    boolean validateColumn(char[][] board, int colIdx) {
        int checkBit = 0;
        for (int i = 0; i < board.length; i++) {
            char num = board[i][colIdx];
            if (num == '.') continue;
            int toCheckBit = (int) Math.pow(2, num-'0');
            if ((checkBit & toCheckBit) != 0) return false;
            checkBit = checkBit | toCheckBit;
        }
        return true;
    }

    boolean validateSquare(char[][] board, int leftUpperEdgeX, int leftUpperEdgeY) {
        int checkBit = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                char num = board[leftUpperEdgeX + i][leftUpperEdgeY + j];
                if (num == '.') continue;;
                int toCheckBit = (int) Math.pow(2, num-'0');
                if ((checkBit & toCheckBit) != 0) return false;
                checkBit = checkBit | toCheckBit;
            }
        }
        return true;
    }

}
