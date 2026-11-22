# ABOTA Digital

Primeira fatia demonstrativa de uma aplicação para gestão de grupos de abota. A interface usa dados de exemplo claramente identificados; ainda não regista operações financeiras reais.

## Estrutura

- `frontend/`: React, TypeScript/TSX, Vite, PWA e configuração Capacitor.
- `backend/`: API Python/FastAPI e modelos SQLAlchemy/PostgreSQL.
- `render.yaml`: definição inicial da API e da base PostgreSQL no Render.

## Desenvolvimento frontend

```bash
pnpm install
pnpm dev
```

Para compilar: `pnpm build`. A PWA está preparada com manifesto e service worker; no iPhone, abrir o endereço publicado no Safari e usar Partilhar → Adicionar ao ecrã principal.

## API local

A partir da raiz, crie um ambiente virtual e instale `backend/requirements.txt`. Em seguida execute `uvicorn app.main:app --app-dir backend --reload --port 8000`. A verificação de saúde fica em `/health`; a documentação OpenAPI em `/api/docs`. Defina `DATABASE_URL` e `CORS_ORIGINS` no ambiente, nunca em ficheiros versionados.

## Android

A configuração Capacitor usa o identificador `com.abotadigital.app`. Instale/prepare o Android SDK, execute `pnpm android:sync` e abra o projeto Android gerado com `pnpm android:open`. Assinatura APK e distribuição exigem configuração de keystore e ferramentas Android próprias.

## Render

`render.yaml` prepara um Web Service Python e PostgreSQL. Antes de criar recursos, rever região/plano/custos no Render e definir `CORS_ORIGINS` com a origem da aplicação web. A configuração não contém chaves secretas. A integração persistente PostgreSQL, autenticação e migrações devem ser finalizadas antes de usar dados reais.
