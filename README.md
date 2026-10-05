# BI Executivo de Concessões Hidroviárias

Repositório privado para desenvolvimento e implantação controlada do BI Executivo de Concessões Hidroviárias.

## Estrutura
- `public/`: interface e dados de fontes públicas.
- `server/`: protótipo de servidor e configuração de exemplo.
- `private/`: somente estrutura vazia/modelo. **Não versionar dados internos reais, documentos SEI, credenciais ou segredos.**
- arquivos de controle: fontes oficiais, fila de validação, histórico e rotina de atualização.

## Segurança
Este repositório não substitui autenticação institucional. O servidor incluído é um scaffold de teste. Para uso com dados internos, implantar em ambiente privado com HTTPS, autenticação institucional, controle de perfis e auditoria.

## Versão inicial
Base: v8 — Implantação Privada. Data de corte da base pública: 03/10/2026.


## Integração com o BI Hidrovias
Este repositório compõe o mesmo painel executivo do repositório [bi-hidrovias](https://github.com/hzhcdyvz4w-tech/bi-hidrovias).

- **BI Hidrovias**: carteira de investimentos, execução física/orçamentária/financeira, contratos, auditorias, SEI e demais visões operacionais.
- **BI Concessões Hidroviárias**: estudos/modelagens/concessões, marcha processual, participação social, decisões, comunidades e respectivos processos SEI.

A integração deve preservar a separação de segurança: o repositório **bi-hidrovias é público** e o **bi-concessoes-hidroviarias é privado**. Por isso, arquivos internos, dados SEI ou informações sensíveis não devem ser copiados para o repositório público. O vínculo entre os dois painéis é lógico/navegacional, com compartilhamento apenas de referências públicas e campos compatíveis.
