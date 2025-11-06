# CRAFT Text Detector - Version Mise à Jour

## ⚠️ Mise à Jour Importante

Ce projet est une version mise à jour de la librairie Python `craft-text-detector` existante qui n'était plus compatible avec les versions modernes de NumPy et PyTorch. La librairie originale était devenue non fonctionnelle avec les environnements Python récents.

**Cette version corrigée est maintenant compatible avec :**
- NumPy >= 1.21
- PyTorch >= 2.0
- OpenCV >= 4.5
- Python 3.8+

## Description

CRAFT (Character Region Awareness for Text detection) est un détecteur de texte basé sur deep learning qui peut localiser des régions de texte individuelles dans des images naturelles. Cette implémentation PyTorch permet une détection de texte précise dans diverses conditions.

## Fonctionnalités

- ✅ Détection de texte en temps réel
- ✅ Support des images de toutes tailles
- ✅ Détection de texte courbé et orienté
- ✅ Mode GPU et CPU
- ✅ Export des résultats en différents formats
- ✅ Compatible avec les versions récentes de NumPy et PyTorch

## Installation

### Installation depuis ce repository (Recommandé)

```bash
# Cloner le repository
git clone https://github.com/votre-username/CRAFT-pytorch.git
cd CRAFT-pytorch

# Installer en mode développement
pip install -e .
```

### Installation des dépendances manuellement

```bash
pip install torch>=2.0 opencv-python>=4.5 numpy>=1.21
```

## Utilisation Rapide

```python
import craft_text_detector

# Charger les modèles
craft_net = craft_text_detector.load_craftnet_model(cuda=False)
refine_net = craft_text_detector.load_refinenet_model(cuda=False)

# Lire une image
image = craft_text_detector.read_image('path/to/your/image.jpg')

# Obtenir les prédictions
predictions = craft_text_detector.get_prediction(
    image=image,
    craft_net=craft_net,
    refine_net=refine_net,
    text_threshold=0.7,
    link_threshold=0.4,
    low_text=0.4,
    cuda=False,
    long_size=1280
)

# Les résultats contiennent:
# - masks: masques de détection
# - boxes: coordonnées des boîtes
# - boxes_as_ratios: coordonnées normalisées
# - polys_as_ratios: polygones normalisés
# - heatmaps: cartes de chaleur
# - times: temps d'exécution
```

## Utilisation avec la classe Craft

```python
from craft_text_detector import Craft

# Initialiser le détecteur
craft = Craft(
    output_dir='outputs/', 
    crop_type="poly",
    cuda=False
)

# Prédire sur une image
predictions = craft.detect_text('path/to/image.jpg')
```

## Structure du Projet

```
craft_text_detector/
├── __init__.py          # Interface principale
├── craft_utils.py       # Utilitaires CRAFT
├── file_utils.py        # Gestion des fichiers
├── image_utils.py       # Traitement d'images
├── predict.py           # Logique de prédiction
├── torch_utils.py       # Utilitaires PyTorch
└── models/              # Architectures des modèles
    ├── craftnet.py      # Modèle CRAFT principal
    ├── refinenet.py     # Modèle de raffinement
    └── basenet/         # Réseaux de base
        └── vgg16_bn.py  # VGG16 avec BatchNorm
```

## Paramètres Principaux

- `text_threshold`: Seuil de confiance pour le texte (défaut: 0.7)
- `link_threshold`: Seuil de confiance pour les liens (défaut: 0.4)
- `low_text`: Score minimal pour le texte (défaut: 0.4)
- `cuda`: Utiliser GPU si disponible (défaut: False)
- `long_size`: Taille maximale pour l'inférence (défaut: 1280)
- `poly`: Activer la détection polygonale (défaut: True)

## Changements par Rapport à la Version Originale

1. **Compatibilité NumPy** : Correction des appels dépréciés à NumPy
2. **Compatibilité PyTorch** : Mise à jour pour PyTorch 2.0+
3. **Gestion des types** : Amélioration du typage et de la gestion des erreurs
4. **Performance** : Optimisations pour les versions récentes des dépendances

## Problèmes Résolus

- ❌ `AttributeError: module 'numpy' has no attribute 'int'` → ✅ Corrigé
- ❌ Incompatibilité avec PyTorch 2.0+ → ✅ Corrigé
- ❌ Problèmes de shapes avec NumPy récent → ✅ Corrigé
- ❌ Warnings de dépréciation → ✅ Corrigé

## Contribution

Cette version est maintenue pour corriger les problèmes de compatibilité. Les contributions sont les bienvenues via les pull requests.

## Licence

Ce projet maintient la même licence que le projet CRAFT original.

## Crédits

- Projet original CRAFT : [lien vers le paper/repo original]
- Mise à jour et maintenance : [Votre nom]

## Support

Si vous rencontrez des problèmes avec cette version mise à jour, veuillez ouvrir une issue sur ce repository.

---

**Note**: Cette version corrigée vous permet d'utiliser CRAFT avec les environnements Python modernes sans les erreurs de compatibilité de la librairie originale.
