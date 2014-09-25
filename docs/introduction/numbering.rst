..  This file is part of Invenio
    Copyright (C) 2014 CERN.

    Invenio is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation; either version 2 of the
    License, or (at your option) any later version.

    Invenio is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Invenio; if not, write to the Free Software Foundation, Inc.,
    59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


.. _introduction-numbering:

Release Numbering Scheme
------------------------

The official Invenio repository contains several branches for
maintenance and development purposes.  We roughly follow the usual git
model as described in
`man 7 gitworkflows <http://www.kernel.org/pub/software/scm/git/docs/gitworkflows.html>`_
and elsewhere.

===================== ===================== ======================
major                 minor                 patchlevel
===================== ===================== ======================
important rewrites    new features          bug fixes only
new functionality     APIs evolution        no change to APIs
major API changes     DB schema evolution   stable DB
===================== ===================== ======================

In summary, the new patchlevel releases (X.Y.Z) happen from the
``maint`` branch, the new minor feature releases (X.Y) happen from the
``master`` branch, and new major feature releases (X) happen after they
mature in the ``next`` branch.  A more detailed description follows.


Development Repository Branches
```````````````````````````````

``maint``
~~~~~~~~~

This is the maintenance branch for the latest stable release.  There
can be several maintenance branches for every release series
(**maint-0.99**, **maint-1.0**, **maint-1.1**), but typically we use only
``maint`` for the latest stable release.

The code that goes to the maintenance branch is of bugfix nature only.  It
should not alter DB table schema, Invenio config file schema, local
configurations, or template function parameters in a backward-incompatible
way.  If it contains any new features, then they are switched off in order
to be fully compatible with the previous releases in this series.
Therefore, for installations using any Invenio released X.Y series, it
should be always safe to upgrade the system at any moment in time by (1)
backing up their folder containing local configuration, (2)
installing the corresponding ``maint-X.Y`` branch updates, and (3) rolling
back the configuration folder with their customizations.

``master``
~~~~~~~~~~

The ``master`` branch is where the new features are being developed and
where the new feature releases are being made from.  The code in
``master`` is reviewed and verified, so that it should be possible to make
a new release out of this branch almost at any given point in time.
However, Invenio installations that would like to track this branch should
be aware that DB table definitions are not frozen and may change, the
config is not frozen and may change, etc, until the release time.  So
while ``master`` is relatively stable for usage, it should be treated with
extreme care, because updates between day D1 and day D2 may require DB
schema and configuration changes that are not covered by usual update
statements, so people should be prepared to study the differences and
update DB schemata and config files themselves.

``next``
~~~~~~~~

If a new feature is well implemented, tested and considered stable, it
goes directly into the ``master`` branch described previously.  If it is
cleaned, tested and almost stable, but not fully ``master`` worthy yet,
then it may go to the ``next`` branch.  The ``next`` branch serves as a
kind of stabilization branch for ``master``.  The features may stay in
``next`` for a long enough time to get stabilized, and when they
are ready, they are promoted to ``master`` (or to ``maint`` in some
scenarios).  The code in ``next`` may have bugs, may not pass the test
suite, but anyway should be stable enough so that it is almost never
revoked/rebased.

Usually, ``master`` contains all of ``maint``, and ``next`` contains all of
``master``.  This is assured by periodical upward merges
(maint-to-master, master-to-next, etc).
