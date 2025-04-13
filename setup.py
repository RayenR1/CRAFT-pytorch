from setuptools import setup

setup(
    name="craft_pytorch_custom",  # Changez le nom pour éviter les conflits
    version="0.1",
    packages=["craft_text_detector"],  # Nom du dossier contenant les .py
    install_requires=[  # Liste des dépendances (ex: torch, opencv)
        "torch",
        "opencv-python",
        "numpy",
    ],
)