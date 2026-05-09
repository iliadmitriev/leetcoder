
use std::collections::HashSet;

impl Solution {
    pub fn validate_coupons(
        code: Vec<String>,
        business_line: Vec<String>,
        is_active: Vec<bool>,
    ) -> Vec<String> {
        let valid_business_lines: HashSet<&str> =
            ["electronics", "grocery", "pharmacy", "restaurant"].into();

        let mut valid_codes: Vec<_> = business_line
            .into_iter()
            .zip(code)
            .zip(is_active)
            .filter(|((business, code), is_active)| {
                *is_active
                    && !code.is_empty()
                    && valid_business_lines.contains(business.as_str())
                    && code.chars().all(|c| c.is_alphanumeric() || c == '_')
            })
            .collect();

        valid_codes.sort();
        valid_codes.into_iter().map(|((_, code), _)| code).collect()
    }
}