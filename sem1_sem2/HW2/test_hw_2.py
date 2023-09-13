from checker import checkout
from checker import calc_crc32

folder_out = "/home/sk/out"


def test_step1():
    res1 = checkout("cd {};7z x arx2.7z".format(folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "test1")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    assert (checkout("cd {};7z l arx2.7z".format(folder_out), "test2")), "test2 FAIL"


def test_step3():
    assert (checkout("cd {};7z h arx2.7z".format(folder_out), calc_crc32(None, 'hash_crc'))), "Test1 FAIL"