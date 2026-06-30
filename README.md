# Anjou Bitcoin

## Lancer le projet

1. Installer [Jekyll](https://jekyllrb.com/docs/installation/#requirements)

2. Lancer la commande : 
`bundle exec jekyll serve`

## Contribuer

Workflow Git :

- **Développement** sur des branches de _dev_ (une par sujet/correctif).
- **Pré-production** : on merge sur la branche `release` pour validation.
- **Déploiement** : on merge `release` sur `main` (branche de production déployée par Netlify).

Prévisualisations Netlify :

- Chaque branche de _dev_ et la branche `release` disposent d'un **déploiement de
  prévisualisation** Netlify (branch deploys), pour relire le rendu avant de promouvoir
  vers `main`.
- Les pull requests génèrent également une **Deploy Preview**.

## Arborescence du projet

- _includes : structure des pages 
- _layout : structure des pages 
- _posts : articles du site web
- _sass : style des pages
- _site : repertoire dans lequel est généré le code static
- assets : repertoire dans lequels se trouve les images, codes Javascript, styles CSS, polices d'écritures.
- _config.yml : configuration du projet
- _headers : configuration des headers côté serveur
- sitemap.xml : plan du site pour le réferencement
- Fichiers .md / .html : pages du site web

## Rédaction d'un article 

- Création d'un fichier dans le repertoire /_posts avec la syntaxe AAAA-MM-JJ-titre.md
- Rédaction de l'article avec le format Markdown (.md)
- Ajout des images de l'article dans le répertoire assets/images/articles/{titre article}/
- Ajout de l'article sur le fichier sitemap.xml pour le référencement