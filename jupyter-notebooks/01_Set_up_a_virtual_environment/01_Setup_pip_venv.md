# Környezet kialakítása csomagok telepítése

## 1. Virtual environment - venv

Amikor egy új python projektbe kezdünk, érdemes ehhez egy saját "virtuális környezetet" létrehozni, és ebbe telepíteni a később felhasznált csomagokat.

A legnagyobb előnye, hogy így ha pl később frissíteni akarunk egy csomagot, akkor a **korábban megírt kódunkat ez nem fogja befolyásolni**, a saját virtuális környezetéhez tartozó csomagok érintetlenül maradnak, a **kód továbbra is ugyanúgy fog futni.**

Ezeknek a kezelése Anacondából is lehetséges, de röviden megmutatom a parancssoros verziót a Python beépített venv moduljával.

## 2. Csomagok telepítése - pip

Elkészült a virtuális környeztünk, így következhet a projekthez szükséges csomagok telepítése. Először a már korábban látott *"pip list"* paranccsal ellenőrizhetjük az újonnan létrehozott környezetünk tartalmát. Láthatjuk, **hogy nem teljesen üres, hiszen a `pip` például már telepítve van,** de erre szükségünk is lesz a további csomagok telepítéséhez.

Maga a `pip` a Python Package Manager, amivel telepíthetjük, frissíthatjük, törölhetjük vagy listázhatjuk a telepített csomagokat.

### 2.1 Telepítés egyessével

Kezdhetjük például a `matplotlib` telepítésével. Fontos kihangsúlyozni, hogy az virtuális környezetben telepített csomagok **csak itt elérhetőek,** az alap Python csomagok közé nem kerülnek be.

```
python -m pip install matplotlib
python -m pip install matplotlib==3.4.3
```

A parancs kiadását követően, ha ismételten megnézzük a telepített csomagok listáját, akkor láthatjuk, hogy nem csak a `matplotlib` került bele, hanem több más könyvtár is. Ez azért van, mert a telepítés során az összes "függőség" is települ, azaz azok a csomagok, amikre a matplotlibnek is szüksége van.

### 2.2 Telepítés lista alapján

A csomagokat nem csak egyesével lehet telepíteni. Lehetőségünk van **"requiremets.txt"** file-ba gyűjtött összes szükséges csomag telepítésére a következő paranccsal:

```
python -m pip install -r requirements.txt
```

Ebben a file-ban nem csak a csomagok nevei, de a verziói is listázhatók, így tudjuk azt a verziót telepíteni mindenből, amivel a kódunk működni fog. A projekthez használt csomagok a Jupyter Notebook mellett egy "requiremets.txt"-ben megtalálható, és ez alapján telepíthetőek.

### 2.3 Lista exportálása

A virtuális környezetünkbe telepített programok listáját ki is menthetjük a pip freeze paranncsal:

```
pip freeze > requirement.txt
```

Ebben listázásra kerül környezet összes telepített könyvtára verziószámmal együtt.


Note: venv in Jupiter:

```
pip install --user ipykernel

python -m ipykernel install --user --name=myenv
```
