#!/usr/bin/env python3
"""Scaffold de implantação privada. /api/private permanece bloqueada até autenticação institucional."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, datetime, os
ROOT=Path(__file__).resolve().parent.parent
PUBLIC=ROOT/"public"
LOG=ROOT/"logs"/"auditoria.log"
class Handler(SimpleHTTPRequestHandler):
    def translate_path(self,path):
        rel=path.split("?",1)[0].lstrip("/") or "index.html"
        target=(PUBLIC/rel).resolve()
        if PUBLIC.resolve() not in target.parents and target != PUBLIC.resolve():
            return str(PUBLIC/"__blocked__")
        return str(target)
    def do_GET(self):
        if self.path.startswith("/api/private"):
            self.audit("PRIVATE_DENIED")
            self.send_response(403); self.send_header("Content-Type","application/json; charset=utf-8"); self.end_headers()
            self.wfile.write(json.dumps({"status":"bloqueado","mensagem":"Camada privada exige autenticação institucional configurada no servidor."},ensure_ascii=False).encode())
            return
        self.audit("PUBLIC_GET"); super().do_GET()
    def audit(self,event):
        LOG.parent.mkdir(exist_ok=True)
        with LOG.open("a",encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now().isoformat()} | {event} | {self.client_address[0]} | {self.path}\n")
if __name__=="__main__":
    os.chdir(PUBLIC)
    ThreadingHTTPServer(("127.0.0.1",8080),Handler).serve_forever()
