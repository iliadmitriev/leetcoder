import (
	"unsafe"
)

func toLowerCase(s string) string {
	d := unsafe.Pointer(&s)
	b := *(*[]byte)(d)

	for i := range len(b) {
		if b[i] >= 'A' && b[i] <= 'Z' {
			b[i] += 32
		}
	}

	return s
}
