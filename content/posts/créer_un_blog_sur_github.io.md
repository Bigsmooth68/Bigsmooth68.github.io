---
title: "Créer un Blog sur github.io"
date: 2023-03-25T16:55:39+01:00
tags: ["Hugo","SSG","Tutoriel"]
---

Pour ce premier post, je vais expliquer comment j'ai mis en place ce blog sur gitpage.
<!--more-->
Créer deux repo: BlogSources et Bigsmooth68.github.io. Activer github pages pour ce dernier.

Dans le répertoire de son choix, créer le nouveau site avec la commande hugo (le binaire d'hugo doit être installé au préalable avec, par exemple, chocolatey: `choco install hugo`).
```bash
hugo new site BlogSources
```

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Bigsmooth68/BlogSources.git
git push -u origin main
```

Créer un fichier `.gitignore` à l'aide de toptal.com gitignore:
```bash
https://www.toptal.com/developers/gitignore/api/visualstudiocode,hugo
```

Cloner le repo du thème de son choix:
```bash
git clone https://github.com/lukeorth/poison.git themes/poison --depth=1
```

Mettre à jour le `config.toml` (notamment le thème). Lien [ici](https://github.com/Bigsmooth68/BlogSources/blob/main/config.toml).

Ajouter le repo github dans `public`:
```bash
git submodule add -f https://github.com/Bigsmooth68/Bigsmooth68.github.io public
```

Générer le site:
```bash
hugo -t poison
```

Ajouter l'about:
```bash
hugo new page/about.md
```

Ajouter un post:
```bash
mkdir blog
hugo new posts/créer_un_blog_sur_github.io.md
```

Ajouter le code généré dans le repo:
```bash
cd public
git commit -m 'Initial commit'
git push
```

Patienter quelques secondes que le pipeline mettent à jour le contenu ...

_Référence_: [Creating a Free Blog or Static Content Website with Hugo and GitHub Pages with Custom Domain and Ads](https://www.youtube.com/watch?v=LSJ5S8VG5aU)