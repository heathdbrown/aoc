# SPDX-FileCopyrightText: 2022-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
import click

from ..__about__ import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='aoc')
@click.pass_context
def aoc(ctx: click.Context):
    click.echo('Hello world!')
