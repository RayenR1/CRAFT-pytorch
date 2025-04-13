from setuptools import setup, find_packages
import os

# Fonction pour inclure tous les fichiers nécessaires
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py') and not filename.startswith('__'):
                paths.append(os.path.join('..', path, filename))
    return paths

# Fichiers supplémentaires à inclure
extra_files = package_files('craft_text_detector/models')

setup(
    name="craft_text_detector_custom",
    version="1.0.0",
    packages=find_packages(),
    package_data={
        'craft_text_detector': extra_files + ['*.py'],
    },
    include_package_data=True,
    install_requires=[
        "torch>=2.0",
        "opencv-python>=4.5",
        "numpy>=1.21"
    ],
)