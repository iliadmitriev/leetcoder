import (
	"slices"
	"strings"
)

func removeSubfolders(folder []string) []string {
	res := make([]string, 0, len(folder))

	slices.Sort(folder)

	for _, f := range folder {
		if len(res) == 0 || !strings.HasPrefix(f, res[len(res)-1]+"/") {
			res = append(res, f)
		}
	}

	return res
}
