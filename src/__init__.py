#!/usr/bin/python3
# surf - Building projects for the 21th century.

import yaml
import sys
import os
import click
import httplib2

COMPILERS = {
    ".c": "{file_path}"
    ".cpp"
    ".rs"
    ".go"
    ".zig"
    ".cbl"
    ".cob"
    ".f"
    ".for"
    ".f90"
    ".f95"
    ".jakt"
    ".adb"
    ".ads"
    ".d"
    ".m"
    ".mm"
    ".swift"
}
GCC = {}
LLVM = {}

def project_ccommand(command):
    pass #TODO

def resolver(url):
    if url.startswith('file:'):
        path = url[5:]
        if not os.path.exists(path):
            raise Exception('File not found: ' + path)
        else:
            return path
    elif url.startswith('url:'):
        url = url[4:]
        h = httplib2.Http()
        resp, content = h.request(url)
        if resp.status != 200:
            raise Exception('Error fetching url: ' + url)
        else:
            v = content
            f = open('/tmp/surf-url-%s' % url, 'w+')
            f.write(v)
    elif url.startswith('env:'):
        env = url[4:]
        if env not in os.environ:
            raise Exception('Environment variable not found: ' + env)
        else:
            v = os.environ[env]
            f = open('/tmp/surf-env-var-%s' % env, 'w+')
            f.write(v)
            return '/tmp/surf-env-var'
    else:
        raise Exception('Unknown url type for %s' % url)

@click.group("cli")
@click.pass_context
def surf_cli():
    """Building and mantaining projects for the 21st century."""
    pass

@click.command("build exec", help="Build the current project as an executable")
def cli_build_exec():
    project_ccommand("build_exec")
    pass

@click.command("build lib", help="Build the current project as a library (so/dll/dylib)")
def cli_build_lib():
    project_ccommand("build_lib")
    pass

@click.command("build ape", help="Build the current project as an αcτµαlly pδrταblε εxεcµταblε")
def cli_build_ape():
    project_ccommand("build_ape")
    pass


@click.command("clean", help="Clean the current project build")
def cli_clean():
    project_ccommand("clean")
    pass

@click.command("test", help="Build (and run) the current project's tests")
def cli_test():
    pass

@click.command("install", help="Install the compiled version of the current project")
def cli_install():
    pass

@click.command("uninstall", help="Uninstall the installed of the current project")
def cli_uninstall():
    pass

@click.command("check", help="Check if the current project is configured.")
def cli_check():
    pass

@click.command("edit", help="Edit the current project's SURF file.")
def cli_edit():
    pass

@click.command("autobuild", help="Start AutoBuild for the current project")
def cli_autobuild():
    pass

surf_cli.add_command(cli_build_exec)
surf_cli.add_command(cli_build_ape)
surf_cli.add_command(cli_build_lib)
surf_cli.add_command(cli_clean)
surf_cli.add_command(cli_test)
surf_cli.add_command(cli_install)
surf_cli.add_command(cli_uninstall)
surf_cli.add_command(cli_check)
surf_cli.add_command(cli_edit)
surf_cli.add_command(cli_autobuild)

if __name__ == '__main__':
    surf_cli()