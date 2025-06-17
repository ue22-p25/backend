# slides réseau / backend

les slides du cours réseau / backend à l'École des Mines de Paris

## Slides

elles sont faites avec `remark.js` qui part de sources en `markdown`
voir <https://github.com/gnab/remark/wiki> à propos de ce qu'on peut mettre dans le markdown

## Template HTML

chaque slideshow vient avec, par exemple `slides1.html` et `slides1.md`  
le html charge remark.js, et le markdown, qui est transformé en html par remark.js  

du coup tous les html sont semblables, on les a factorisés dans `template.html`:

```bash
# pour mettre à jour les html
python template_run.py
```

si sur macos, on peut obtenir une sorte de mode *watch* en faisant

```bash
echo template.html | entr -rp python template_run.py
```

## Développement

```bash
# start vite dev server
npm run dev

# then in another terminal
open http://localhost:nnnn/index.html
```

## warnings

### slides3

WIP - not reviewed yet
