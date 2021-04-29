"""
File: marsweight.py
"""

MARS_MULTIPLE = .378

def main():
    earth_weight = float(input('Enter a weight on earth: '))
    mars_weight = earth_weight * MARS_MULTIPLE
    print('The equivalent weight on Mars: ', mars_weight)

if __name__ == '__main__':
    main()
