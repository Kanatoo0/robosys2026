#!/bin/bash
# SPDX-FileCopyrightText: 2026 Kanato Aketagawa
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目のテスト失敗"
    res=1
}

res=0

out=$(printf 'def hello():\n    print("Hello")\n' | ./indentcheck 2>/dev/null)
[ "$?" = 0 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf 'def hello():\n  print("Hello")\n' | ./indentcheck 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf 'def hello():\n\tprint("Hello")\n' | ./indentcheck 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf '' | ./indentcheck 2>/dev/null)
[ "$?" = 0 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf 'def hello():\n  print("Hello")\n   print("World")\n' | ./indentcheck 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf '    print("Hello")\n' | cat | ./indentcheck 2>/dev/null)
[ "$?" = 0 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit "$res"
