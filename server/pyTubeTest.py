import requests
import os
import pytube
from halo import Halo
from pathlib import Path
from enum import Enum

"""VARS"""
#url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

url = "https://www.youtube.com/watch?v=dQw4w9"
class State:

    PATH_STATE: bool = True
    DOWNLOAD_STATE: bool = True

class Test_Suite:

    """
    Test Suite for making sure that your code isn't broken
    """

    def __init__(
        self,
        win_path=None,
        linux_path=None,
        spinner=Halo(color="white", text="Testing PyTube", spinner="dots"),
    ):
        self.win_path = win_path
        self.linux_path = linux_path
        self.spinner = spinner

    def WhoAmI(self):
        """
        Takes in PATH and decide the winner.
        """

        if self.win_path and self.linux_path == None:
            State.PATH_STATE = 0
            raise AssertionError("No Path Found")
        elif self.win_path != None:
            home_dir = self.win_path
            self.spinner.succeed(text="Windows Path Detected")
            self.spinner.start()
            return home_dir
        elif self.linux_path != None:
            home_dir = self.linux_path
            self.spinner.succeed(text="Linux Path Detected")
            self.spinner.start()
            return home_dir

    def GetDownloadsFolder(self):
        """
        Returns the default downloads path for linux or windows

        This will ensure that if someone contributes we can get an accurate pass or fail
        independant of the operating system
        """

        print("\n---Testing Suite---\n   ---PyTube---\n")
        self.spinner.start()

        if os.name == "nt":
            import winreg

            sub_key = (
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
            )
            downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                self.win_path = winreg.QueryValueEx(key, downloads_guid)[0]
            return

        else:
            self.linux_path = os.path.join(os.path.expanduser("~"), "downloads")
            return

    def Test(self, url, home_dir):
        """
        Test Method in Test_Suite Class
        Used to validate that the site will work
        """

        # we can not assume that the site is up so get and assert
        _req = requests.get(url)
        _filename = "pytube-test"

        """
        Assert that both we can reach the url, and that the home_dir is not of NoneType, or > 5
        """
        assert _req.status_code == 200
        self.spinner.succeed(text="Site online -> PASS")
        self.spinner.start()
        assert len(home_dir) > 5
        self.spinner.succeed(text="Path Assertion -> PASS")
        self.spinner.start()

        a = os.path.join(home_dir, _filename) + ".mp4"
        if os.path.isfile(a):
            os.remove(a)

        try:
            _youtube = pytube.YouTube(url=url)
        except:
            self.spinner.fail(text="Could not reach URL -> FAIL\n")
            self.spinner.stop()
            State.DOWNLOAD_STATE = 0

        if os.path.isfile(a):
            self.spinner.fail(text="File Exists")
            self.spinner.stop()
            State.PATH_STATE = 0

        """for testing purposes we do not care about resolution
            for this case we will use a low-pixel res for effeciency

            Another thing, the pytube code is inherently broken.
            the fix is in extract.py line: 301

            parse_qs(formats[i]["signatureCipher"]) -> instead of "cipher"
        """

        try:
            video = _youtube.streams.get_lowest_resolution()
            video.download(output_path=home_dir, filename=_filename)
        except:
            self.spinner.fail(text="Test Failed because video download -> FAILED\n")
            self.spinner.stop()
            State.DOWNLOAD_STATE = 0
        if os.path.isfile(a):
            self.spinner.succeed(text="Video Download -> PASS")
            self.spinner.start()
        else:
            self.spinner.fail(text="Download Failed -> file does not exist\n")
            self.spinner.stop()
            State.DOWNLOAD_STATE = 0

        self.spinner.start()
        self.spinner.stop()

        # Check if anything fails for CI
        if State.DOWNLOAD_STATE == 0:
            print("")
            self.spinner.info(text="Tests Failed")
            self.spinner.stop()
            print("")
            return False
        elif State.PATH_STATE == 0:
            print("")
            self.spinner.info(text="Tests Failed")
            self.spinner.stop()
            print("")
            return False
        else:
            print("")
            self.spinner.info(text="Tests Passed")
            self.spinner.stop()
            print("")
            return True


if __name__ == "__main__":
    suite = Test_Suite()
    suite.GetDownloadsFolder()
    home_dir = suite.WhoAmI()
    r = suite.Test(url, home_dir)
    if r == False:
        exit(1)
