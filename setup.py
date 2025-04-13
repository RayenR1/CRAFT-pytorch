from setuptools import setup

setup(
    name="craft_text_detector_custom",
    version="1.0.0",
    packages=["craft_text_detector"],
    package_data={"craft_text_detector": ["*.py"]},
    install_requires=[
        "torch",
        "opencv-pytho4.5",
        "numpy"
    ],
)