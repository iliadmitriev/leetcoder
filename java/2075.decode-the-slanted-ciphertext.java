class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        if (rows == 1) {
            return encodedText;
        }

        int n = encodedText.length();
        int cols = n / rows;
        StringBuilder buf = new StringBuilder();

        for (int start = 0; start < cols; start++) {
            for (int i = 0, j = start; i < rows && j < cols; i++, j++) {
                buf.append(encodedText.charAt(i * cols + j));
            }
        }

        return buf.toString().stripTrailing(); // unicode aware trim
        
    }
}