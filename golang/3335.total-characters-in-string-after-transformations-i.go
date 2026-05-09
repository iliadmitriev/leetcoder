func lengthAfterTransformations(s string, t int) int {
	const N = int('z' - 'a' + 1)
	const MOD = int(1e9 + 7)
	var res int
	var cnt [N]int

	full, extra := t/N, t%N

	for _, c := range s {
		cnt[c-'a']++
	}

	for range full {
		tmp := cnt[N-1]

		for i := N - 1; i > 0; i-- {
			cnt[i] = (cnt[i] + cnt[i-1]) % MOD
		}

		cnt[0] = (cnt[0] + tmp) % MOD
		cnt[1] = (cnt[1] + tmp) % MOD
	}

	// add extra to result
	for i := N - 1; i >= N-extra; i-- {
		res = (res + cnt[i]) % MOD
	}

	for i := range N {
		res = (res + cnt[i]) % MOD
	}

	return res
}
