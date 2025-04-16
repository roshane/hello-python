from seleniumbase import SB

CHROME_PATH = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'


def main():
    with SB(test=True, uc=True, binary_location=CHROME_PATH) as sb:
        sb.open('https://google.com')
        sb.type('textarea#APjFqb', 'seleniumbase')
        sb.click(
            'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')
        sb.sleep(120)


# with SB(test=True, uc=True):
if __name__ == '__main__':
    main()
