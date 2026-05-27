import zipfile, os, base64, sys

# 📦 Estructura y contenido
DIR = "plugin.video.victor.hub"
os.makedirs(DIR, exist_ok=True)

addon_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.victor.hub" name="Victor Hub" version="1.0.0" provider-name="Victor">
    <requires><import addon="xbmc.python" version="3.0.0"/></requires>
    <extension point="xbmc.python.pluginsource" library="main.py">
        <provides>video executable</provides>
    </extension>
    <extension point="xbmc.addon.metadata">
        <summary>Hub personal de Victor</summary>
        <platform>all</platform>
    </extension>
</addon>"""

main_py = """# -*- coding: utf-8 -*-
import sys, xbmc, xbmcgui, xbmcplugin

BASE_URL, HANDLE = sys.argv[0], int(sys.argv[1])
MIS_ADDONS = [
    ("⚫ Blackghost", "plugin://plugin.video.blackghost/", "https://bluegray25.github.io/", "Streaming"),
    ("🔓 Resolver", "plugin://plugin.video.resolver/", "https://michaz1988.github.io/repo/", "Resolvedor"),
    ("🧥 Balandro", "plugin://plugin.video.balandro/", "https://repobal.github.io/base/", "Español"),
    ("🧭 Magellan", "plugin://plugin.video.magellan/", "https://tinyurl.com/magellanrepo/", "Horus variant"),
    ("⚔️ Espada Drago", "plugin://plugin.video.espada.drago/", "https://dregs1.github.io/", "IPTV"),
    ("🌆 Skyline", "plugin://plugin.video.skyline/", "https://bugatsinho.github.io/repo/", "Variado"),
    ("🧲 Elementum", "plugin://plugin.video.elementum/", "https://elementumorg.github.io/", "P2P"),
    ("🧪 f4mTester", "plugin://plugin.video.f4mtester/", "https://kodiloucosbr.github.io/", "Tester"),
    ("🦅 Horus GTKing", "plugin://plugin.video.horus/", "https://gtkingbuild.github.io/", "Phoenix Team"),
]

def build_url(act, **p): return f"{BASE_URL}?action={act}" + "".join(f"&{k}={v}" for k,v in p.items())

def list_addons():
    xbmcplugin.setContent(HANDLE, 'files')
    li = xbmcgui.ListItem(label="📦 Victor Hub"); li.setInfo('video', {'Plot': 'Pulsa para ejecutar. Mantén para opciones.'})
    xbmcplugin.addDirectoryItem(HANDLE, "", li, False)
    for n, u, r, d in MIS_ADDONS:
        aid = u.replace("plugin://", "").rstrip("/")
        li = xbmcgui.ListItem(label=n); li.setInfo('video', {'Plot': f"{d}\\n🔗 {r}\\n🆔 {aid}"})
        li.addContextMenuItems([("🔗 Copiar repo", f"RunPlugin({build_url('copy', url=r)})"), ("🔍 Verificar", f"RunPlugin({build_url('check', aid=aid)})")])
        xbmcplugin.addDirectoryItem(HANDLE, u, li, True)
    xbmcplugin.endOfDirectory(HANDLE)

def copy(u):
    xbmc.executebuiltin(f'SetClipboard("{u}")')
    xbmcgui.Dialog().notification("✓ Victor Hub", "URL copiada", xbmcgui.NOTIFICATION_INFO, 2000)
    xbmcplugin.endOfDirectory(HANDLE)

def check(a):
    ok = bool(xbmc.getCondVisibility(f'System.HasAddon({a})'))
    xbmcgui.Dialog().ok("🔍 Victor Hub", f"{a}\\n{'✅ Instalado' if ok else '❌ No instalado'}")
    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    p = dict(x.split('=',1) for x in sys.argv[2][1:].split('&') if '=' in x) if len(sys.argv)>2 and sys.argv[2] else {}
    a = p.get('action')
    if a == 'copy': copy(p.get('url',''))
    elif a == 'check': check(p.get('aid',''))
    else: list_addons()
"""

# Icono 1x1 transparente
with open(f"{DIR}/icon.png", "wb") as f: f.write(base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="))
with open(f"{DIR}/addon.xml", "w", encoding="utf-8") as f: f.write(addon_xml)
with open(f"{DIR}/main.py", "w", encoding="utf-8") as f: f.write(main_py)

# Genera ZIP
with zipfile.ZipFile("plugin.video.victor.hub.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(DIR):
        for file in files:
            z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "."))

print("✅ ZIP creado: plugin.video.victor.hub.zip")