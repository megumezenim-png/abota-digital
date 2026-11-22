# Entregas do ABOTA Digital

## 1. Dashboard mensal e informação financeira legível
- O dashboard apresenta o grupo e ciclo ativos, mês e ano visíveis, número de participantes, contribuição individual, total esperado, total confirmado, total pendente, pagamentos confirmados, beneficiários do mês, valor previsto por beneficiário e progresso do ciclo.
- Os valores financeiros são sempre acompanhados da moeda FCFA.
- O dashboard de demonstração identifica claramente os dados como fictícios e não apresenta qualquer pagamento como real.
- O participante consulta resumos; o administrador dispõe de ações rápidas para registar pagamento, adicionar membro e gerir a abota.

## 2. Navegação responsiva e experiência PWA
- A navegação principal inclui Início, Membros, Abota/Calendário, Pagamentos e Perfil.
- No telemóvel a navegação principal fica na parte inferior, os cartões/listas ficam em uma coluna, os botões são acessíveis ao polegar e tabelas são apresentadas como listas.
- No computador a navegação pode usar sidebar fixa e apresentar tabelas/painéis com espaço adequado.
- A aplicação inclui manifesto e suporte de instalação PWA; a experiência funciona em browser móvel, com instruções de instalação no iPhone via Safari.
- A interface usa a paleta verde profundo `#153B32`, verde `#236B54`, verde suave `#E9F3ED`, dourado `#D6A84B`, cinza claro `#F5F7F6` e branco; estados usam texto/ícones além de cor.

## 3. Membros e perfis
- Todos os utilizadores autorizados podem consultar a lista de membros e os perfis permitidos.
- A lista de membros permite pesquisa e filtros Todos, Ativos e Inativos, apresentando avatar, nome, identificador e estado.
- O perfil mostra apenas dados necessários: nome, identificador, estado, entrada no grupo e resumo do histórico; não expõe telefone, endereço, dados bancários, documentos ou outros dados privados não autorizados.
- A gestão de adicionar, editar, ativar/desativar ou remover membros é reservada ao administrador na experiência de demonstração.

## 4. Calendário da abota e beneficiários
- O calendário mostra os meses do ciclo, ano/período, beneficiários, ordem, valor previsto por beneficiário e estado do mês.
- Meses passados são históricos, o mês atual é destacado e meses futuros apresentam previsões.
- Os detalhes do mês mostram o estado dos pagamentos, total arrecadado e esperado, beneficiários e histórico de alterações disponível.
- O sistema valida a compatibilidade entre participantes, meses e beneficiários antes de iniciar um ciclo.
- Alterações na ordem dos beneficiários são reservadas ao administrador e devem deixar histórico; nunca são silenciosas.

## 5. Registo e consulta de pagamentos
- O participante pode consultar o valor mensal, o seu estado e os resumos de pagamentos do grupo, mas não pode alterar estados.
- O administrador pode registar valor pago, mês/ano, data, método/observação opcionais e estados Pago, Pendente ou Parcial, bem como corrigir registos preservando o histórico.
- Pagamentos não são confirmados automaticamente; antes de guardar pede-se confirmação.
- Após confirmar, apresenta-se “Pagamento registado com sucesso.”; o histórico regista responsável e data/hora.
- Pendências e inconsistências ficam visíveis; nenhuma ação altera registos automaticamente.

## 6. Histórico, atividade e notificações de interface
- Registos de alterações identificam quem alterou e quando, incluindo alterações de pagamento e beneficiários.
- O painel de atividade pode mostrar pagamento confirmado, beneficiário atualizado, membro adicionado e ciclo encerrado.
- A interface permite visualizar notificações demonstrativas de pagamento, novo mês, beneficiários e atualizações do grupo, com indicação de leitura.

## 7. Ciclos e arquivo anual
- O administrador pode consultar uma revisão final de encerramento com pagamentos, recebimentos e pendências visíveis.
- Os ciclos encerrados ficam arquivados em modo de consulta, preservando membros, contribuições mensais, pagamentos confirmados/pendentes/parciais, beneficiários, valores, resumo e alterações.
- O histórico não permite edição direta nem apagamento silencioso.

## 8. Backend Python/PostgreSQL para Render
- O backend é Python/FastAPI com API REST versionada, persistência PostgreSQL e modelos para grupos, ciclos, membros, contribuições, beneficiários e auditoria.
- O esquema e as alterações de base de dados são versionados por migrações; a configuração de Render não inclui credenciais no repositório.
- A URL da API e CORS são configuráveis; frontend mantém demonstração funcional sem credenciais.
- A autenticação real e validação das permissões no servidor são requisitos antes de dados reais, não simulados como concluídos na primeira fatia.

## 9. Empacotamento Android
- A aplicação web é preparada para ser envolvida com Capacitor e inclui instruções de build Android para gerar APK.
- A assinatura e distribuição do APK são identificadas como dependentes do SDK Android e das credenciais de assinatura, sem alegar APK assinado se não for gerado.

## 10. Segurança e limites de demonstração
- A aplicação não movimenta nem custodia dinheiro real.
- Antes de utilizar dados reais, são necessários autenticação segura, permissões no servidor, backups/recuperação, proteção de dados e validação legal/operacional.
- A ordem de recebimento, alterações, erros e ações administrativas têm feedback explícito e claro.
