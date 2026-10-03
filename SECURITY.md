# Segurança do BI Executivo de Concessões Hidroviárias

## Classificação
Este repositório é privado, mas não deve ser tratado como cofre de documentos internos.

## Não versionar
- documentos ou anexos SEI;
- dados pessoais ou informações restritas;
- senhas, tokens, chaves, cookies ou credenciais;
- arquivos reais de `private/`;
- configurações locais, logs, candidatos e snapshots.

## Camada privada
O arquivo versionado em `private/` é somente um modelo (`dados_internos.example.json`).
Dados internos reais só poderão ser utilizados após implantação em ambiente institucional com HTTPS, autenticação server-side, autorização por perfil e auditoria.

## Publicação
A pasta `public/` deve conter exclusivamente informação apta à exposição pública. Alterações materiais passam pela fila de validação antes de publicação.

## Incidente
Se um segredo ou dado interno for incluído por engano, interromper a publicação, revogar/rotacionar a credencial quando aplicável e tratar também o histórico Git.
