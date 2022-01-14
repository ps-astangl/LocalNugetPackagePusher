import sys

from NugetFeedHelper import NugetFeedHelper


def main():
    config = sys.argv[1]
    NugetFeedHelper().run(config)


if __name__ == '__main__':
    main()
