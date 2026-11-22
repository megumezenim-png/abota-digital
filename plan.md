# Plano de implementação — ABOTA Digital

## Objetivo
Construir uma aplicação mobile-first para organizar grupos de abota. A primeira entrega é um MVP navegável com dados inequivocamente demonstrativos, adaptável a browser e ecrãs móveis, instalável como PWA (incluindo iPhone via Safari) e preparado para empacotamento Android APK. Não movimenta nem custodia dinheiro real.

## Arquitetura
- **Frontend** em `frontend/`: React + TypeScript/TSX, Vite e CSS responsivo, manifesto PWA e camada cliente da API configurável por ambiente.
- **Android** em `frontend/` (configuração Capacitor) com destino de projeto nativo em `android/`; build/assinatura final pode exigir SDK Android e credenciais de assinatura.
- **Backend** em `backend/`: Python + FastAPI, API REST versionada, SQLAlchemy, Alembic e PostgreSQL. A configuração `render.yaml` prepara API e base de dados no Render sem guardar credenciais.
- **Configuração da raiz**: workspace pnpm, scripts comuns, documentação, plano, tarefas e configuração Render.
- Frontend é desenvolvido para Preview no Manus; API/PostgreSQL destinam-se a Render por pedido explícito. A publicação efetiva no Render depende de acesso/configuração do utilizador. CORS e URL da API são configuráveis.
- Perfis previstos: administrador e participante. O protótipo pode alternar perspetivas; autenticação e permissões de servidor devem ser implementadas antes de dados reais.

## MVP inicial
Dashboard mensal com progresso e valores FCFA; navegação Início/Membros/Abota/Pagamentos/Perfil; lista pesquisável de membros; calendário do ciclo; estados de contribuições demonstrativas com registo exclusivo do administrador no protótipo; atividade/auditoria e ciclos arquivados em consulta; PWA instalável e estrutura FastAPI/PostgreSQL para ligação posterior.

## Fora da primeira entrega
Movimentação/custódia de dinheiro, integração bancária, pagamentos reais, autenticação de produção, notificações push, publicação efetiva no Render e distribuição/assinatura da Play Store. Dependem de regras, credenciais, segurança e validação legal/operacional.

## Estrutura do repositório
```text
abotadigital/
├── frontend/                 # React/TSX, CSS, PWA e Capacitor
│   ├── public/               # manifesto, ícones e rotas
│   └── src/                  # vistas, componentes e estado
├── backend/                  # FastAPI, requisitos, modelos e migrações
│   └── app/                  # endpoints e aplicação API
├── android/                  # artefactos nativos futuros do Capacitor
├── render.yaml               # serviço e PostgreSQL no Render
├── package.json              # scripts do workspace
├── pnpm-workspace.yaml       # configuração pnpm
├── plan.md / TODO.md         # plano aprovado e critérios por entregar
└── README.md                 # instruções de execução/build
```

## Direção de design
- **Movimento:** fintech contemporânea minimalista, com clareza editorial e referências a interfaces de gestão financeira.
- **Princípios:** confiança sem aparência bancária pesada; transparência nos estados e valores; ações curtas e explícitas; informação reorganizada para mobile.
- **Cores:** verde profundo `#153B32`, verde `#236B54`, verde suave `#E9F3ED`, dourado `#D6A84B`, fundo `#F5F7F6`, branco. Estados têm texto/ícones além de cor.
- **Layout:** navegação inferior e cartões/listas no telefone; sidebar e painéis de detalhe em ecrãs largos; evitar tabelas apertadas no mobile.
- **Elementos distintivos:** marca circular abstrata de contribuições que convergem; trilho de progresso mensal; acento dourado reservado a beneficiários/recebimentos.
- **Interação/animação:** ações financeiras explícitas com confirmação e feedback; transições curtas; sem alteração automática de registos.
- **Tipografia:** Manrope para títulos e Inter para texto e valores, em semibold quando financeiros.
- **Essência:** “A abota do grupo, clara e organizada num só lugar.” Personalidade: confiável, simples, transparente.
- **Tom:** direto e próximo. Exemplos: “Acompanha a tua abota, mês a mês.” “Pagamento registado com sucesso.”
- **Marca/logótipo:** wordmark ABOTA em Manrope semibold e símbolo próprio de círculos ligados num ciclo.
- **Cor de assinatura:** verde profundo `#153B32`.

## Limites
Antes de dados reais, definir atrasos/saídas/alterações de beneficiários, validar privacidade/autenticação e confirmar quem pode alterar registos. Não incluir credenciais Render no repositório.
