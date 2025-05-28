from setuptools import setup, find_packages

setup(
    name="sign-language-translation",
    version="0.1.0",
    description="Real-time Sign Language Translation System",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Yash Khandelwal",
    author_email="",
    url="https://github.com/YashKhandelwal0705/Sign-Language-Translation-System",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask>=3.1.1',
        'opencv-python>=4.11.0.86',
        'numpy>=1.26.4',
        'ultralytics>=8.3.14',
        'mediapipe>=0.10.21'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Processing'
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'sign-language=Flask App.app:main'
        ]
    }
)
