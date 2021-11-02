# Dash alkalmazás: példák és bevezetés

A Dash-t és a Plotly-t ugyanaz a csapat fejleszti.
Ezzel a csomaggal viszonlag könnyen készíthetünk webalaklmazást főleg adatmegjelenítési céllal.

Telepítés:

    pip install dash


Egy kis inspirációnak érdemes megnézni a Dash-el készölt alkalmazások listáját:
https://dash.gallery/Portal/


A Plotly-hoz hasonlóan a Dash is nagyon jól dokumentált:
https://dash.plotly.com/introduction

## 01_Basic_example

https://dash.plotly.com/layout
30 sor kód, és kész a webapp!
Nem túl komplex, de működik.

Érdekességek:
 * app = dash.Dash(__name__)
 * HTML layout
 * Debug mode (auto refresh) 

## 02_Dash_core_components

https://dash.plotly.com/layout
Ez a példa megmutatja, hogy hogyan lehet a beviteli mezőket definiálni, amiket aztán a plotok frissítéséhez használhatunk.

 * Label
 * Dropdown
 * Radioitems
 * Checklist
 * Input
 * Slider
 * Br

## 03_Callbacks_basics

https://dash.plotly.com/basic-callbacks
Ez a példa megmutatja az Input, Output és State callback legegyszerűbb használatát.

A callback-ek használata python dekorátorok segítségével működik.
 * Input: a fuggvény bemenete, érékének változásakor lefut a függvény és frissül az Output
 * State: a fuggvény bemenete, érékének változásakor NEM fut le fut a függvény, csak tárolja az új értéket
 * Output: a függvény visszatérési értéke ezt frissíti

## 04_Callbacs_with_figure

https://dash.plotly.com/basic-callbacks

Ez a példa egy olyan plotot mutat, amit összesen 5 input is képes befolyásolni.
Importált style használata.


További érdekes példák:
* Interaktív plot hover info vagy kijelölés alapján: https://dash.plotly.com/interactive-graphing
* Globális változó helyett adattárolás a 'session'-ben https://dash.plotly.com/sharing-data-between-callbacks

