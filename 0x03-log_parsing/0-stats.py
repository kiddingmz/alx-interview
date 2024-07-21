#!/usr/bin/python3
"""Log parser"""
import sys
from typing import List, Union
import re


def validate_line(log: str) -> Union[List[str], None]:
    """Check whether a line is skippable"""
    line = log.split(" ")
    if len(line) != 9:
        if "-" in line[0]:
            clean = log.replace("-", " - ", 1)
            line = clean.split(" ")
        else:
            return None

    try:
        # Validate IP Address
        ip_address = line[0]
        ip_pattern = r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"
        if not re.match(ip_pattern, ip_address) and ip_address != "Holberton":
            return None

        # Validate date
        date = " ".join([line[2][1:], line[3][:-1]])
        date_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}"
        if not re.match(date_pattern, date):
            return None

        # Validate endpoint
        endpoint = " ".join([line[4], line[5], line[6]])
        if endpoint != '"GET /projects/260 HTTP/1.1"':
            return None

        # Validate file size
        try:
            file_size = int(line[8])
        except (ValueError, IndexError):
            file_size = None
        if not file_size:
            return None
    except IndexError:
        return None

    return line


def parse_lines(lines: List[str]):
    """Parse some lines from stdin"""
    if not lines:
        print("File size: 0")
        return
    file_size = 0
    status_codes_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    for log in lines:
        line = validate_line(log)
        if line is None:
            continue
        try:
            size = int(line[8])
        except (ValueError, IndexError):
            size = None
        if size:
            file_size += size
        try:
            status_code = int(line[7])
        except (ValueError, IndexError):
            status_code = None
        if status_code and status_code in status_codes_count.keys():
            status_codes_count[status_code] += 1
    print("File size: {}".format(file_size))
    for key, value in status_codes_count.items():
        if value != 0:
            print("{}: {}".format(key, value))


def extract_lines():
    """Read a given number of lines from standard input"""
    lines = []
    try:
        count = 1
        while True:
            line = sys.stdin.readline().rstrip()
            if not line:
                linesLength = len(lines)
                if linesLength > 0 and linesLength % 10 != 0:
                    parse_lines(lines)
                if linesLength == 0:
                    parse_lines(lines)
                break
            lines.append(line)
            if count == 10:
                parse_lines(lines)
                count = 0
            count += 1
    except KeyboardInterrupt:
        parse_lines(lines)


if __name__ == "__main__":
    extract_lines()
