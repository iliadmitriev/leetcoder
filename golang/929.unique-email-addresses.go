func numUniqueEmails(emails []string) int {
	cache := make(map[string]bool, len(emails))

	for _, email := range emails {
		v := strings.Split(email, "@")
		localName, domainName := v[0], v[1]
		localName = strings.Split(localName, "+")[0]
		localName = strings.ReplaceAll(localName, ".", "")
		unifiedEmail := strings.Join([]string{localName, domainName}, "@")

		cache[unifiedEmail] = true
	}

	return len(cache)
}
