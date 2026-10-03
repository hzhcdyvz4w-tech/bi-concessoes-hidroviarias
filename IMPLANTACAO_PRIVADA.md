# BI Executivo de Concessões Hidroviárias — v8

## Arquitetura
- `public/`: somente dados que podem ser expostos.
- `private/`: estrutura interna, atualmente vazia.
- `server/`: camada de servidor e configuração de segurança.
- `logs/`: auditoria.
- `MATRIZ_ACESSO.csv`: perfis e permissões.

## Regra de segurança
A versão entregue **não cria senha padrão** e **não libera a camada privada**.
A rota privada retorna 403 até que seja integrada a autenticação institucional.

## Implantação recomendada
1. Hospedar em ambiente institucional/privado com HTTPS.
2. Integrar autenticação institucional (SSO/IdP ou solução aprovada pela TI).
3. Restringir a pasta `private/` ao servidor; ela nunca deve ser servida como arquivo estático.
4. Aplicar os perfis LEITOR, ANALISTA, GESTOR e ADMIN.
5. Manter logs de acesso e alteração.
6. Só depois importar processos/documentos internos autorizados.
7. Manter qualquer publicação externa sem arquivos da pasta privada.

## Teste local
`python server/app.py`
A interface pública abre em `localhost:8080`. A API privada permanece bloqueada.

## Próxima etapa
Integrar o mecanismo de autenticação escolhido e criar o importador autorizado da Base-Mãe/SEI.
