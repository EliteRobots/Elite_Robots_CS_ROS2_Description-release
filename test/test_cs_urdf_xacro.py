# Author: Chen Shichao

from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

import pytest
from ament_index_python.packages import get_package_share_directory


@pytest.mark.parametrize("cs_type", [
    "cs63", "cs63a", "cs66", "cs66a", "cs68", "cs612", "cs616",
    "cs618f", "cs620", "cs625", "cs630", "cs520h", "ls65",
])
@pytest.mark.parametrize("prefix", ["", "left_"])
def test_cs_urdf_xacro(cs_type, prefix, tmp_path):
    share = Path(get_package_share_directory("elite_robots_description"))
    subdir = "urdf_5f" if cs_type.endswith("h") else "urdf"
    result = subprocess.run([
        "xacro", str(share / subdir / "cs.urdf.xacro"),
        f"name:={cs_type}", f"cs_type:={cs_type}", f"tf_prefix:={prefix}",
        "use_fake_hardware:=true", "safety_limits:=true",
    ], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    urdf = tmp_path / "robot.urdf"
    urdf.write_text(result.stdout)
    check = subprocess.run(["check_urdf", str(urdf)], capture_output=True, text=True)
    assert check.returncode == 0, check.stderr

    robot = ET.fromstring(result.stdout)
    joints = [j for j in robot.findall("joint") if j.attrib["type"] != "fixed"]
    assert len(joints) == (5 if cs_type.endswith("h") else 6)
    assert all(j.attrib["name"].startswith(prefix) for j in joints)
    for mesh in robot.findall(".//mesh"):
        uri = mesh.attrib["filename"]
        assert uri.startswith("package://"), uri
        package, relative = uri[len("package://"):].split("/", 1)
        assert (Path(get_package_share_directory(package)) / relative).is_file(), uri
