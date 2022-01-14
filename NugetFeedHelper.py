import subprocess
import os
import logging as logger
import re
import configparser


class NugetFeedHelper:
    def __init__(self):
        logger.basicConfig(format='%(message)s', level=logger.DEBUG)
        self.configuration = ""
        self.major_version = 0
        self.minor_version = 0
        self.micro_version = 0
        self.nuget_exe = ""
        self.package_name = ""
        self.project_path = ""
        self.local_feed = ""
        self.parsed_config = configparser.ConfigParser()

    @staticmethod
    def process_command(command: str) -> subprocess.CompletedProcess:
        string_args = command.split(" ")
        return subprocess.run(string_args, capture_output=True)

    @staticmethod
    def find_file(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def set_state_from_config(self):
        self.parsed_config.read("config.ini")
        self.nuget_exe = self.parsed_config[self.configuration]["Nuget"]
        self.project_path = self.parsed_config[self.configuration]["ProjectPath"]
        self.local_feed = self.parsed_config[self.configuration]["LocalFeed"]
        self.package_name = self.parsed_config[self.configuration]["PackageName"]
        return self

    def check_local_feed_dir(self) -> None:
        logger.info("Searching for Local Nuget Feed: {0}".format(self.local_feed))
        if os.path.exists(self.local_feed):
            return None
        else:
            logger.info("Unable to locate Directory {0}".format(self.local_feed))
            self.process_command("mkdir {0}".format(self.local_feed))
            return None

    def set_current_version_from_nuget_list(self, process: subprocess.CompletedProcess):
        nuget_artifact = str(process.stdout)
        matched_version_number = re.findall(re.compile(r"(\d+).(\d+).(\d+)"), nuget_artifact)[0]
        version = [int(version_number) for version_number in matched_version_number]
        self.major_version = version[0]
        self.minor_version = version[1]
        self.micro_version = version[2]
        return self

    def auto_update_micro(self):
        self.micro_version += 1
        return self

    def create_version_string(self) -> str:
        return "{0}.{1}.{2}".format(self.major_version, self.minor_version, self.micro_version)

    def create_package(self):

        self.set_state_from_config()

        nuget_list_command = "{0} list -s Local {1}".format(self.nuget_exe, self.package_name)

        logger.info("Searching for Package {0} in nuget feed".format(self.package_name))

        logger.info("{0}".format(nuget_list_command))

        result_nuget_list_command = self.process_command(nuget_list_command)

        self.set_current_version_from_nuget_list(result_nuget_list_command)

        self.auto_update_micro()

        raw_pack = "dotnet pack {0} -p:PackageVersion={1}".format(self.project_path, self.create_version_string())

        logger.info("{0}".format(raw_pack))

        raw_pack_result = self.process_command(raw_pack)

        pkg_name = "{0}.{1}.{2}".format(self.package_name, self.create_version_string(), "nupkg")

        raw_pack_result.check_returncode()

        built_nuget_package = self.find_file(pkg_name, os.path.dirname(self.project_path))

        logger.info("Pushing {0} to Feed {1}".format(built_nuget_package, self.local_feed))

        raw_push = "dotnet nuget push {0} -s {1}".format(str(built_nuget_package), str(self.local_feed))

        push_result = self.process_command(raw_push)

        logger.info(str(push_result.stdout))

    def run(self, configuration: str):
        self.configuration = configuration
        return self.create_package()