=========
 invtool
=========

-------------------------------------------------------------------
A Command Line Interface for poking at Mozilla's Inventory project.
-------------------------------------------------------------------

Notes On Installing
===================

``invtool`` requires ``requests`` and ``simplejson`` (and ``argparse`` if you are running python2.6)::

    sudo pip install -r requirements.txt
    sudo python setup.py install

An optional package (though highly recommend and included in
``requirements.txt``) is ``keychain``. If you need to use ``invtool`` without
it, remove it from ``requirements.txt`` and store your ldap password in
plaintext.

``invtool`` supports a few different ways of setting your credentials. Your
username can either be stored in the configuration file or passed at the
command line. Your password may be stored in the configuration file (in
plain text), stored in a `python-keyring <https://pypi.python.org/pypi/keyring>`_,
or passed on the command line. If you do not want to store your credentials
on disk at all, you must remove the ldap_username AND ldap_password entries
from the configuration file.

``invtool`` will look for a configuration file at ``./etc/invtool.conf`` and
if it can't find anything there, ``/etc/invtool.conf``.

Here is a quick tip for a non-root install::

    git clone git@github.com:uberj/inv-tool.git invtool
    cd invtool
    export PYTHONPATH=.:$PYTHONPATH
    ln -s ./bin/invtool ./devinvtool
    ./devinvtool status

On this first invocation, if no credentials have been previously set, invtool
will prompt you for them. If the keyring module is present, your password will
be stored in the system keyring for later use under the service
"invtool-ldap". The keyring service name can be changed in the configuration
file.

RTFM
====

``man invtool`` OR checkout the repo and run ``make man``.
