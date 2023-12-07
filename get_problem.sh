#!/bin/bash

if test -f "$PWD/cookie.txt"; then
    cookie=$(<cookie.txt)
else
    echo "No saved cookie found, please enter session cookie from adventofcode.com"
    read cookie
    if [[ -z "${cookie}" ]]; then
        echo "No cookie entered, aborting."
        exit 0
    fi
    echo "$cookie" > "$PWD/cookie.txt"
fi

current_year=$(date '+%Y')

get_problem() {
    if [[ ! -d "$1" ]]; then
        mkdir "$1"
    fi

    if [[ ! -d "$1/$2" ]]; then
        mkdir "$1/$2"
    fi
    {
        curl "https://adventofcode.com/$1/day/$2/input" -H "cookie: session=$cookie" --compressed --output "$1/$2/input.txt"
        } &> /dev/null

    echo "Problem input written to ./$1/$2/input.txt"
    echo "Problem instructions can be found at: https://adventofcode.com/$1/day/$2"

}

exit_msg(){
    echo ""
    echo "Usage: $(basename "${BASH_SOURCE[0]}") [year] [day]"
    echo ""
    echo "Gets the Advent Of Code problem from year and day"
    echo "If no year and day are provided, the program will default to today's date"
    exit 1
}

if [[ $# -eq 0 ]]; then # No parameters specified, default to today
    monthday=$(date '+%m %d')
    if [[ "$monthday" < "12 01" ]] || [[ $monthday > "12 25" ]]; then
        echo "Advent Of Code is not running right now, try specifying a year and problem."
        exit_msg
    else
        year=$current_year
        day=$(echo $(date '+%d') | sed 's/^0*//')
    fi
elif [[ $# -eq 2 ]]; then
    if [[ $1 -lt 2015 ]] || [[ $1 -gt $current_year ]]; then
        echo "Invalid Year: $1, valid years are 2015-$current_year"
        exit_msg
    elif [[ $2 -lt 1 ]] || [[ $2 -gt 25 ]]; then
        echo "Invalid Day: $2, valid days are 1-25"
        exit_msg
    else
        year=$1
        day=$(echo $2 | sed 's/^0*//')
    fi
fi

get_problem $year $day