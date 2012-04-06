= pygeos =

This repository is a fork of django.contrib.gis.geos tracked with git-svn and
patched to be usable without django installed.

== Notes ==

=== Initializing svn repository ===

    cp .gitconfig .git/config (or copy manually the git-svn section)
    git svn fetch

=== Merging upstream changes ===

    git svn rebase
