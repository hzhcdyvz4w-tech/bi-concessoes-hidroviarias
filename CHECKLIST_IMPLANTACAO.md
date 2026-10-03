# Checklist de implantação controlada

- [x] Repositório GitHub privado
- [x] Separação entre camada pública e estrutura privada
- [x] Sem senha padrão
- [x] Rota privada bloqueada no scaffold
- [x] Segredos, logs, dados internos, candidatos e snapshots ignorados pelo Git
- [x] Modelo privado separado do arquivo real
- [ ] Hospedagem institucional definida
- [ ] HTTPS configurado
- [ ] SSO/IdP institucional integrado
- [ ] Perfis LEITOR/ANALISTA/GESTOR/ADMIN validados pela TI
- [ ] Auditoria server-side implantada
- [ ] Política de backup/retenção aprovada
- [ ] Teste de acesso por celular e computador
- [ ] Importador de dados internos autorizado e testado

**Regra:** não importar SEI nem informação interna real antes de concluir os itens de infraestrutura e autenticação.
