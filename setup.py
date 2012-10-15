#!/usr/bin/env python

import os
import sys
import subprocess

from setuptools import setup
from setuptools.command.install import install

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("virtual-node")


class node_install(install):
    env_dir = os.environ['VIRTUAL_ENV']
    default_version = '0.8.11'
    verbose = False

    def run(self):
        self.install_node(self.env_dir)

    def get_node_src_url(self, version, postfix=''):
        node_name = 'node-v%s%s' % (version, postfix)
        tar_name = '%s.tar.gz' % (node_name)
        if version > "0.5.0":
            node_url = 'http://nodejs.org/dist/v%s/%s' % (version, tar_name)
        else:
            node_url = 'http://nodejs.org/dist/%s' % (tar_name)
        return node_url

    def run_cmd(self, cmd, cwd=None, extra_env=None):
        """
        Execute cmd line in sub-shell
        """
        all_output = []
        cmd_parts = []

        for part in cmd:
            if len(part) > 45:
                part = part[:20] + "..." + part[-20:]
            if ' ' in part or '\n' in part or '"' in part or "'" in part:
                part = '"%s"' % part.replace('"', '\\"')
            cmd_parts.append(part)
        cmd_desc = ' '.join(cmd_parts)
        logger.debug(" ** Running command %s" % cmd_desc)

        # output
        stdout = subprocess.PIPE

        # env
        if extra_env:
            env = os.environ.copy()
            if extra_env:
                env.update(extra_env)
        else:
            env = None

        # execute
        try:
            proc = subprocess.Popen(
                [' '.join(cmd)], stderr=subprocess.STDOUT, stdin=None, stdout=stdout,
                cwd=cwd, env=env, shell=True)
        except Exception:
            e = sys.exc_info()[1]
            logger.error("Error %s while executing command %s" % (e, cmd_desc))
            raise

        stdout = proc.stdout
        while stdout:
            line = stdout.readline()
            if not line:
                break
            line = line.rstrip()
            all_output.append(line)
            logger.info(line)
        proc.wait()

        # error handler
        if proc.returncode:
            for s in all_output:
                logger.critical(s)
            raise OSError("Command %s failed with error code %s"
                % (cmd_desc, proc.returncode))

        return proc.returncode, all_output


    def install_node(self, env_dir, version=None):
        """
        Download source code for node.js, unpack it
        and install it in virtual environment.
        """
        version = version or self.default_version
        logger.info(' * Install node.js (%s' % version,
                             extra=dict(continued=True))

        node_name = 'node-v%s' % (version)
        node_url = self.get_node_src_url(version)

        src_dir = os.path.join(env_dir, 'src')
        node_src_dir = os.path.join(src_dir, node_name)
        env_dir = os.path.abspath(env_dir)

        if not os.path.exists(node_src_dir):
            os.makedirs(node_src_dir)

        cmd = [
            'curl', '--silent', '-L', node_url, '|',
            'tar', 'xzf', '-', '-C', src_dir,
        ]
        try:
            self.run_cmd(cmd, env_dir)
            logger.info(') ', extra=dict(continued=True))
        except OSError:
            postfix = '-RC1'
            logger.info('%s) ' % postfix, extra=dict(continued=True))
            new_node_url = self.get_node_src_url(version, postfix)
            cmd[cmd.index(node_url)] = new_node_url
            self.run_cmd(cmd, env_dir)

        logger.info('.', extra=dict(continued=True))

        conf_cmd = [
            './configure',
            '--prefix=%s' % (env_dir),
        ]

        self.run_cmd(conf_cmd, node_src_dir)
        logger.info('.', extra=dict(continued=True))
        self.run_cmd(['make'], node_src_dir)
        logger.info('.', extra=dict(continued=True))
        self.run_cmd(['make install'], node_src_dir)

        logger.info(' done.')

setup(
    name='virtual-node',
    version='0.0.1',
    description='Install node.js into your virtualenv',
    author='Sebastian Vetter',
    author_email='sebastian@roadside-developer.com',
    url='http://github.com/elbaschid/virtual-node',
    long_description=open('README.rst', 'r').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: JavaScript',
        'Topic :: Software Development :: Libraries',
    ],
    license='BSD',
    cmdclass={
        'install': node_install,
    }
)
