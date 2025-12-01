package readline

import (
	"slices"
	"testing"
)

func TestReadLines(t *testing.T) {
	lines := Readlines("test.txt")
	if !slices.Equal(lines, []string{"foo", "bar", "baz"}) {
		t.Errorf("lines we read do not match")
	}
}
