class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        def unifyEmail(email: str) -> str:
            plusIdx = -1
            atIdx = -1
            for i in range(len(email)):
                if plusIdx == -1 and email[i] == "+":
                    plusIdx = i
                if atIdx == -1 and email[i] == "@":
                    atIdx = i

            if plusIdx == -1:
                plusIdx = atIdx

            localName, domainName = email[:plusIdx], email[atIdx + 1:]
            localName = "".join(ch for ch in localName if ch != ".")

            print(email, localName, domainName)

            return f"{localName}@{domainName}"

        res = set()
        for email in emails:
            res.add(unifyEmail(email))

        return len(res)

