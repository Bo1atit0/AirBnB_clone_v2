from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of a web_static folder"""

    # Create versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate timestamp filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Generate archive path
    archive_path = "versions/{}".format(archive_name)

    # Compress the web_static folder into .tgz archive
    result = c.local("tar -cvzf {} web_static".format(archive_path))

    # Check result
    if result.failed:
        return None
    return archive_path

