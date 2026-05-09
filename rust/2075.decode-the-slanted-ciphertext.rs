impl Solution {
    pub fn decode_ciphertext(encoded_text: String, rows: i32) -> String {
       if rows == 1 {
        return encoded_text;
       }

       let rows = rows as usize;
       let cols = encoded_text.len() / rows;
       let chars: Vec<char> = encoded_text.chars().collect();

       (0..cols)
        .flat_map(|start| {
          let chars = &chars;

          (0..rows)
            .take_while(move |&i| start + i < cols)
            .map(move |i| chars[i * cols + start + i])
        })
        .collect::<String>()
        .trim_end()
        .to_string()
    }
}