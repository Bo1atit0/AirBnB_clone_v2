#!/usr/bin/python3
"""
Write a Fabric script that generates a
.tgz archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of a web_static folder"""

    # create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # generate timestamp filename
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time_stamp)

    # Generate archive path
    archive_path = "versions/{}".format(archive_name)

    # compress the webstatic folder into .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    # check result
    if result.failed:
        return None
    else:
        return archive_path

