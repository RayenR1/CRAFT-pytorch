from setuptools import setup, find_packages

setup(
    name="craft_text_detector_custom",
    version="1.0.1",  # Changez la version à chaque modification
    packages=find_packages(include=['craft_text_detector*']),
    include_package_data=True,
    install_requires=[
        "torch>=2.0",
        "opencv-python>=4.5",
        "numpy>=1.21"
    ],
)