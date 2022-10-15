package main

import (
	"fmt"
	"net/url"
)

func fetchWayback(domain string) ([]string, error) {

	fetchURL := fmt.Sprintf("http://web.archive.org/cdx/search/cdx?url=*%s/*&output=json&collapse=urlkey\", domain")

	var wrapper [][]string
	err := fetchJSON(fetchURL, &wrapper)
	if err != nil {
		return []string{}, err

	}

	out := make([]string, 0)

	skip := true
	for _, item := range wrapper {
		// skip the first since it's just a string
		if skip {
			skip = false
			continue

		}

		if len(item) < 3 {
			continue
		}

		u, err := url.Parse(item[2])
		if err != nil {
			continue
		}

		out = append(out, u.Hostname())

	}

	return out, nil

}
