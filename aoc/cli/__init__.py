# SPDX-FileCopyrightText: 2022-present Heath Brown <heathd.brown@gmail.com>
#
# SPDX-License-Identifier: MIT
from pathlib import Path

import click
from dotenv import load_dotenv
import requests

load_dotenv()

from ..__about__ import __version__


URL = "https://adventofcode.com"


def create_session():
    s = requests.Session()
    return s


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.argument("year")
@click.argument("day")
@click.option("-s", "--session", envvar="AOC_SESSION")
@click.version_option(version=__version__, prog_name="aoc")
@click.pass_context
def aoc(ctx: click.Context, day, year, session):
    click.echo(f"Year: {year}, Day: {day}")
    click.echo("creating files and tests")

    directory = Path(f"./aoc/year{year}/day{day}/")
    directory.mkdir(parents=True, exist_ok=True)

    click.echo(f"Created directory: ./aoc/year{year}/day{day}")

    filename = Path(f"./aoc/year{year}/day{day}/__init__.py")
    filename.touch(exist_ok=True)

    click.echo(f"Created filename: ./aoc/year{year}/day{day}/__init__.py")

    test_directory = Path("./tests/")
    test_directory.mkdir(parents=True, exist_ok=True)

    test_filename = Path(f"./tests/test_{year}_day{day}.py")
    test_filename.touch(exist_ok=True)
    click.echo(f"Created filename: ./tests/test_{year}_day{day}.py")

    sess = create_session()
    cookie = requests.cookies.RequestsCookieJar()
    cookie.set("session", session, domain="adventofcode.com", path="/")
    resp = sess.get(f"{URL}/{year}/day/{day}/input", cookies=cookie)
    try:
        resp.raise_for_status()
        input_directory = Path("./data")
        input_directory.mkdir(parents=True, exist_ok=True)

        input_filename = Path(f"./data/input_{year}_day{day}.txt")
        input_filename.touch()

        with open(input_filename, "w") as f:
            f.write(resp.text)
        click.echo("Downloaded the data for the day...")
    except requests.exceptions.HTTPError:
        click.echo("Error with download occurred")
