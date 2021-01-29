# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------

# This script parses release version from Git tag and set the parsed version to
# environment variable, REL_VERSION.

import os
import sys

gitRef = os.getenv("GITHUB_REF")
tagRefPrefix = "refs/tags/v"

with open(os.getenv("GITHUB_ENV"), "a") as githubEnv:
    if gitRef is None or not gitRef.startswith(tagRefPrefix):
        githubEnv.write("REL_VERSION=edge\n")
        print ("This is daily build from {}...".format(gitRef))
        sys.exit(0)

    releaseVersion = gitRef[len(tagRefPrefix):]
    releaseNotePath="docs/release_notes/v{}.md".format(releaseVersion)

    if gitRef.find("-rc.") > 0:
        print ("Release Candidate build from {}...".format(gitRef))
    else:
        # Set LATEST_RELEASE to true
        githubEnv.write("LATEST_RELEASE=true\n")
        print ("Release build from {}...".format(gitRef))

    githubEnv.write("REL_VERSION={}\n".format(releaseVersion))