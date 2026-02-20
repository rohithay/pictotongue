from setuptools import setup, find_packages

setup(
    name='pictotongue',
    version='0.1.0',
    description='Extract text from images and translate to any language',
    author='rohithay',
    license='Mozilla Public License 2.0',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'Pillow>=9.0.0',
        'pytesseract>=0.3.10',
        'deep-translator>=1.11.4',
        'opencv-python>=4.5.0',
        'numpy>=1.20.0',
    ],
    keywords=['ocr', 'translation', 'image-to-text', 'accessibility'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
    ],
)
